from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts = []
article_links = []
article_upvotes = []

articles =  soup.select(selector="span.titleline > a")

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_value = max(article_upvotes)
most_upvoted_index = article_upvotes.index(max_value)

print(article_upvotes[most_upvoted_index])
print(article_texts[most_upvoted_index])
print(article_links[most_upvoted_index])





# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# name = soup.select_one(selector="#name")
# print(name.getText())

# headings = soup.select(".heading")
# print(headings)