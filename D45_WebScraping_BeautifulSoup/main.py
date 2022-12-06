from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())

# ----------------------------- finding using html tag name and attributes ----------------------------- #

# print(soup.p) gets only first paragraph
# print(soup.a) gets only first anchor tag

# all_anchor = soup.find_all(name="a")
# print(all_anchor)
# for anchor in all_anchor:
#     print(anchor.getText())
#     print(anchor.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_headings = soup.find_all(name="h3", class_="heading")
# print(section_headings[1].getText())

# ----------------------------- Finding using selectors like CSS selectors ----------------------------- #

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# heading = soup.select_one("#name")
# print(heading)
#
# section_headings = soup.select(".heading")
# print(section_headings)
