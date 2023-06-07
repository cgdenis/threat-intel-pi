from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''The Computer Incident Response Center Luxembourg (CIRCL) is 
a government-driven initiative designed to gather, review, report and respond to 
computer security threats and incidents. https://www.circl.lu/
'''

url = "https://www.circl.lu/doc/misp/feed-osint/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Find all <a> tag containing json using a regular expression
pattern = re.compile(r".*json*")
filtered_paragraphs = soup.find_all('a', string=pattern)
# Print the filtered a href
for paragraph in filtered_paragraphs:
    print(f'OSINT Url: {url}{paragraph.text}')