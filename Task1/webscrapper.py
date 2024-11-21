import requests
from bs4 import BeautifulSoup

url = 'https://cognifyz.com/'  # <-- Replace this link with the website URL you want to scrape

#  Send a GET request to fetch the HTML content of the page
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()  

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific data, such as all headings (e.g., h1, h2, etc.)
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

print("\nHeadings found on the page:")
if headings:
    for heading in headings:
        print(heading.get_text())  # Extract and print the text of each heading
else:
    print("No headings found.")

# Extract all links (URLs in <a> tags)
links = soup.find_all('a', href=True)

print("\nLinks found on the page:")
if links:
    for link in links:
        print(link['href'])  # Print each link URL found on the page
else:
    print("No links found.")
