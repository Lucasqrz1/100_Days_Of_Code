from bs4 import BeautifulSoup
import requests

# Web Scraping: Fetch and parse data from Hacker News homepage
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# Create a BeautifulSoup object to parse HTML content
soup = BeautifulSoup(yc_web_page, "html.parser")

# Extract all article titles from the page
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
# Loop through articles to extract title text and links
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# Extract upvote counts using list comprehension
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Find the article with the most upvotes
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

# Print the title and link of the most upvoted article
print(article_texts[largest_index])
print(article_links[largest_index])


# #Another option to parse data, using local source:
# #import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
#
# # print id
# print(soup.title.name)
#
# # Print a selected string
# print(soup.title.string)
#
# # Indent parsed info
# print(soup.prettify())
#
# # Anchor Tag
# print(soup.a)
#
# # Parse all selected data
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# # Getting hold of the info
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# # Parse particular data
# heading = soup.find_all(name="h1", class_="title")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# # Select the first output
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# # All elements that have a class of "heading"
# soup.select(".heading")
# print(soup.select(".heading"))
