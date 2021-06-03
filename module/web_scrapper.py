from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


req = Request('https://blog.bozho.net')
webpage = urlopen(req).read()

# Parsing
soup = BeautifulSoup(webpage, 'html.parser')

# Formating the parsed html file
# strhtm = soup.prettify()

# Print first 500 lines
# print(soup)
# print(soup.title.string)
# for i in soup.find_all('h2'):


def get_post_links_on_page(bs):
    posts_links = []
    for a in bs.find_all('a', href=True, rel=True):
        if a["rel"][0] == "bookmark":
            posts_links.append(a["href"])

    return set(posts_links)


for i in get_post_links_on_page(soup):
    meh = Request(i)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    break