import csv, requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

with open("quotes.csv", "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["quote", "author"])
	for quote in soup.select (".quote"):
		text = quote.select_one(".text").get_text()
		author = quote.select_one(".author").get_text()
		writer.writerow([text, author])
