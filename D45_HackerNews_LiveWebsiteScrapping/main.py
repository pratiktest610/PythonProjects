from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

articles = soup.select(".titlelink")
article_text = [article.getText() for article in articles]
article_link = [article.get("href") for article in articles]

articles_span = soup.select(".score")
article_upvote = [int(article.getText().split(" ")[0]) for article in articles_span]

# print(article_text)
# print(article_link)
# print(article_upvote)

max_upvotes_index = article_upvote.index(max(article_upvote))

print(article_text[max_upvotes_index])
print(article_link[max_upvotes_index])
print(article_upvote[max_upvotes_index])
