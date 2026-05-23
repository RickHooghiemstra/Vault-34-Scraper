"""
Parses Shopify product descriptionHtml into three parts:
  - description: narrative paragraphs + YouTube embed (no fitment, no specs ul)
  - fitment: plain text extracted from <p><strong>Fitment:</strong>...</p>
  - specs: HTML of the <ul> specs list (empty string if absent)
"""
import json
import re
import sys
from bs4 import BeautifulSoup


def parse_description(html: str) -> dict:
    """Split product descriptionHtml into description, fitment, specs."""
    if not html:
        return {"description": html, "fitment": "", "specs": ""}

    soup = BeautifulSoup(html, "html.parser")

    # --- Extract fitment paragraph ---
    fitment_text = ""
    fitment_tag = None
    for p in soup.find_all("p"):
        strong = p.find("strong")
        if strong and strong.get_text(strip=True).rstrip(":") == "Fitment":
            fitment_tag = p
            # Get everything after "Fitment: " in the paragraph
            full_text = p.get_text(strip=True)
            fitment_text = re.sub(r"^Fitment:\s*", "", full_text).rstrip(".")
            break

    # --- Extract specs <ul> ---
    specs_html = ""
    specs_tag = None
    ul_tags = soup.find_all("ul")
    if ul_tags:
        for ul in ul_tags:
            specs_tag = ul
            # Convert list items to plain text lines
            items = [li.get_text(separator=" ", strip=True) for li in ul.find_all("li")]
            specs_html = "\n".join(items)

    # --- Build new body HTML (narrative + embed, minus fitment + specs) ---
    if fitment_tag:
        fitment_tag.decompose()
    if specs_tag:
        specs_tag.decompose()

    new_body = str(soup)
    # Clean up any double newlines left by removals
    new_body = re.sub(r"\n{3,}", "\n\n", new_body).strip()

    return {
        "description": new_body,
        "fitment": fitment_text,
        "specs": specs_html,
    }


def main():
    # Read JSON array of {id, title, descriptionHtml} from stdin or file
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            products = json.load(f)
    else:
        products = json.load(sys.stdin)

    results = []
    for p in products:
        parsed = parse_description(p.get("descriptionHtml", ""))
        results.append({
            "id": p["id"],
            "title": p.get("title", ""),
            "new_description": parsed["description"],
            "fitment": parsed["fitment"],
            "specs": parsed["specs"],
        })

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
