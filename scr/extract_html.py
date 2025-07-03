from bs4 import BeautifulSoup
import html2text
import re
import ast
import unicodedata


def extract_table_as_markdown(soup):
    """Find all tables and convert each to Markdown tables;
    replace each in the soup with a placeholder."""
    all_tables_markdown = []

    # itérer sur toutes les tables
    for table in soup.find_all('table'):
        md = ""
        rows = []
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 2:
                left = tds[0].get_text(separator=' ', strip=True)
                left = left.lstrip('·').strip()
                right = tds[1].get_text(separator=' ', strip=True)
                rows.append((left, right))
        # Construire la table en Markdown
        if rows:
            md += '|  |  |\n| --- | --- |\n'
            for left, right in rows:
                left = left.replace('|', '\\|').strip()
                right = right.replace('|', '\\|').strip()
                md += f'| {left} | {right} |\n'
            md += '|  |  |\n'
            all_tables_markdown.append(md)
        # Remplacer la table par un placeholder pour indiquer qu'elle a été traitée
        table.replace_with('___MARKDOWN_TABLE_PLACEHOLDER___')

    return soup, all_tables_markdown

def html_to_markdown_with_table(input_html_path, output_md_path):
    with open(input_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    # Use the updated function that processes all tables
    soup, md_tables = extract_table_as_markdown(soup)
    html_with_placeholder = str(soup)
    md = html2text.html2text(html_with_placeholder)
    # Replace each placeholder with the corresponding Markdown table in order
    for md_table in md_tables:
        md = md.replace('___MARKDOWN_TABLE_PLACEHOLDER___', md_table, 1)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(md)


def smart_split_events(text):
    # Step 1: Mask out all parenthesis sections so we never split inside them
    parens = {}
    def _mask_parens(m):
        key = f"§§§{len(parens)}§§§"
        parens[key] = m.group(0)
        return key

    # Mask all parenthesis content
    masked_text = re.sub(r'\([^\)]*\)', _mask_parens, text)

    # Now split on slashes that are NOT between digits (dates) or inside masked parenthesis
    split_candidates = re.split(r'(?<!\d)\s*/\s*(?!\d)', masked_text)

    # Restore parenthesis content
    restored = []
    for part in split_candidates:
        for key, val in parens.items():
            part = part.replace(key, val)
        restored.append(part.strip())

    # Remove empty entries
    events = [e for e in restored if e]

    # If not actually split, just return
    if len(events) == 1:
        return events

    # Further split "smashed" events but keep colons as glue
    final_events = []
    for event in events:
        # Don't split if there's a colon
        if ':' in event:
            final_events.append(event.strip())
            continue
        # Otherwise, try the regex
        subparts = re.findall(r'[A-ZÉÈÎ][\w\s,.\'-:]*\([=+\-/]*\)|[A-ZÉÈÎ][\w\s,.\'-:]+(?: [A-Z][a-z]+)*', event)
        if subparts and len(subparts) > 1:
            final_events.extend([s.strip() for s in subparts if s.strip()])
        else:
            final_events.append(event.strip())

    return final_events

def extract_events(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    sommaire_data = []
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) != 2:
            continue
        # Extract section name, preferring bold text
        section = tds[0].get_text(separator=" ", strip=True)
        bold_section = tds[0].find(['b', 'strong'])
        if bold_section:
            section = bold_section.get_text(separator=" ", strip=True)

        cell = tds[1]
        cell_text = cell.get_text(separator=" ", strip=True)

        # Use the improved splitter
        events = smart_split_events(cell_text)
        # For single-event: try to get bold, else the whole text
        if len(events) == 1:
            bold = cell.find(['b', 'strong'])
            if bold:
                events = [bold.get_text(separator=" ", strip=True)]

        # Only add if section or events non-empty
        if section.strip() or any(e.strip() for e in events):
            sommaire_data.append((section.strip(), [e.strip() for e in events if e.strip()]))

    return sommaire_data

def get_all_events(html_path):
    sommaire = extract_events(html_path)
    list_events = []
    for section, events in sommaire:

        for event in events:
            list_events.append((event))

    return list_events

def remove_titles_from_html(html_path, output_path, titre_NP):
    """
    Removes unwanted titles and their following content in the HTML.
    - For each <p> whose full text (including inside nested tags) matches a title in titre_NP,
      removes that <p> and all content up to and including the next <br> or <p> with only a line break.
    """
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    normalized_titles = [t.lower().strip() for t in titre_NP]

    def matches_title(text):
        if not text:
            return False
        t = text.lower().strip()
        # Remove punctuation for more robust match (optional)
        for wanted in normalized_titles:
            if t.startswith(wanted):
                return True
            # Also allow for the title being in the middle, e.g., "TELENOR ..." or "Telenor (=)"
            if wanted in t:
                return True
        return False

    paragraphs = soup.find_all("p")
    to_remove = set()

    for p in paragraphs:
        full_text = p.get_text(separator=" ", strip=True)  # Get all inner text, spaces normalize
        if matches_title(full_text):
            # Mark this <p> and everything until next <br> or <p> that is a line break
            to_remove.add(p)
            next_node = p.find_next_sibling()
            while next_node:
                # Remove NavigableString that is just whitespace
                if getattr(next_node, 'name', None) is None and str(next_node).strip() == '':
                    _next = next_node.find_next_sibling()
                    to_remove.add(next_node)
                    next_node = _next
                    continue
                # Remove <br> or <p> that is just a line break
                if getattr(next_node, 'name', None) == 'br':
                    to_remove.add(next_node)
                    break
                if getattr(next_node, 'name', None) == 'p':
                    node_text = next_node.get_text(separator=" ", strip=True).lower()
                    if node_text in ["", "&nbsp;", "<o:p></o:p>"]:
                        to_remove.add(next_node)
                        break
                to_remove.add(next_node)
                next_node = next_node.find_next_sibling()

    for node in to_remove:
        try:
            node.decompose()
        except Exception:
            try:
                node.extract()
            except Exception:
                pass

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))


def remove_from_marker(filepath, marker="MARKETING ANALYSTE"):
    """
    Deletes everything in the HTML file from (and including) the first occurrence of marker onwards.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    found = False
    # Walk through all tags in document order
    for tag in soup.find_all(True):
        if found:
            tag.decompose()
            continue
        if marker.lower() in tag.get_text(separator=" ", strip=True).lower():
            # Remove this tag and everything after
            found = True
            tag.decompose()
            # Remove all subsequent siblings of this tag's parent (if any)
            parent = tag.parent
            while parent is not None:
                next_sibling = parent.find_next_sibling()
                while next_sibling:
                    to_remove = next_sibling
                    next_sibling = next_sibling.find_next_sibling()
                    to_remove.decompose()
                parent = parent.parent
            break  # Stop after the first match

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))


def normalize(text):
    text = text.lower().strip()
    text = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in text if not unicodedata.combining(c)])

def add_clients_after_titles(html_path, matrice, output_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    title_to_clients = {normalize(title): clients for title, clients in matrice if clients}

    for p in soup.find_all("p"):
        p_text = normalize(p.get_text(separator=" ", strip=True))
        for title, clients in title_to_clients.items():
            if p_text.startswith(title) and clients:
                client_str = ', '.join(clients)
                new_p = soup.new_tag("p", **{'class': 'MsoNormal'})
                new_span = soup.new_tag(
                    "span",
                    style='font-size:8.0pt; color:#1E9BD7; font-family:"Arial",sans-serif'
                )
                new_span.string = f"Clients: {client_str}"
                new_p.append(new_span)
                p.insert_after(new_p)
                print(f"Added clients for: {title}")  # Debug print
                break

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def divisiontext(text):
    """
    Splits the input text (from the text zone) into a Python list and a summary string.
    Assumes the format is:
    [python list]
    ------
    [summary text]
    Returns (the_list, summary_text)
    """
    # Try to split on "---" or "--------" (handle variable dashes)
    parts = re.split(r'-{3,}', text, maxsplit=1)
    if len(parts) < 2:
        # If no separator found, try to find the end of the list by brackets
        lines = text.strip().splitlines()
        list_lines = []
        rest_lines = []
        in_list = True
        for line in lines:
            if in_list:
                list_lines.append(line)
                if "]" in line:
                    in_list = False
            else:
                rest_lines.append(line)
        list_str = "\n".join(list_lines)
        rest_str = "\n".join(rest_lines).strip()
    else:
        list_str = parts[0].strip()
        rest_str = parts[1].strip()

    try:
        the_list = ast.literal_eval(list_str)
        if not isinstance(the_list, list):
            raise ValueError("Not a list")
    except Exception as e:
        # If parsing fails, return empty list and the whole text as summary
        the_list = []
        rest_str = text.strip()

    return the_list, rest_str

def extract_html():
    print("extract_html function is running")
    
if __name__ == "__main__":
    html_to_markdown_with_table("../data/newsletter.html","../data/newsletter_md.md")
    print(get_all_events('../data/newsletter.html'))