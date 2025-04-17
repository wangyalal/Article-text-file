import requests
from bs4 import BeautifulSoup


def read_links_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file if line.strip()]
        return links
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def extract_text_from_links(links):
    extracted_data = {}

    for link in links:
        try:
            response = requests.get(link)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            text = soup.get_text(strip=True)

            extracted_data[link] = text
            print(f"Successfully extracted text from: {link}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {link}: {e}")
            extracted_data[link] = None

    return extracted_data

if __name__ == "__main__":
    file_path = "web links.txt"

    website_links = read_links_from_file(file_path)

    if website_links:
        extracted_texts = extract_text_from_links(website_links)

        for link, text in extracted_texts.items():
            print(f"\nText from {link}:\n{'-' * 80}\n{text[:5000]}...")