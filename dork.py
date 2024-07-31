import requests
from bs4 import BeautifulSoup
import urllib.parse
import argparse
import time
import random

# Function to perform a Google search query
def google_search(query, num_results=10):
    search_url = "https://www.google.com/search"
    params = {
        'q': query,
        'num': num_results,
        'start': 0  # Start at the first page of results
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # List of possible Google domains
    google_domains = [
        'google.com', 'google.co.uk', 'google.ca', 'google.com.au', 'google.in', 'google.com.br', 'google.co.za',
        'google.com.mx', 'google.fr', 'google.de', 'google.it', 'google.es', 'google.nl', 'google.se', 'google.no'
    ]

    # Randomly select a domain from the list
    google_domain = random.choice(google_domains)
    search_url = f"https://{google_domain}/search"

    try:
        response = requests.get(search_url, params=params, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error occurred while searching for query '{query}': {e}")
        return None

# Function to parse Google search results
def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for item in soup.find_all('div', class_='g'):
        link_tag = item.find('a', href=True)
        title_tag = item.find('h3')
        if link_tag and title_tag:
            link = link_tag['href']
            title = title_tag.get_text()
            snippet = item.find('span', class_='aCOpRe')
            snippet = snippet.get_text() if snippet else 'No snippet available'
            links.append(f"{title}\n{link}\n{snippet}\n")
    return links

# Function to save results to a file
def save_results_to_file(query, links):
    filename = f'{query.replace(" ", "_").replace(":", "_")}.txt'
    with open(filename, 'w') as f:
        for link in links:
            f.write(link + '\n')
    print(f"Results saved to {filename}")

# Main function to perform Google dorking
def main(queries, num_results, delay):
    for query in queries:
        print(f"Searching for query: {query}")
        html = google_search(query, num_results=num_results)
        if html:
            links = parse_results(html)
            print(f"Found {len(links)} results for query '{query}':")
            for link in links:
                print(link)
            print("\n")
            save_results_to_file(query, links)  # Save results to a file
        time.sleep(delay)  # Sleep to avoid rate limiting issues

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform Google dorking to find potential vulnerabilities.")
    parser.add_argument('queries', type=str, nargs='+', help="A list of Google dork queries to run.")
    parser.add_argument('--num_results', type=int, default=10, help="Number of results to retrieve per query (default: 10).")
    parser.add_argument('--delay', type=int, default=10, help="Delay between requests in seconds to avoid rate limiting (default: 10).")

    args = parser.parse_args()

    main(args.queries, args.num_results, args.delay)

