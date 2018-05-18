from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get
from time import sleep
import sys

PHILOSOPHY = ("https://en.wikipedia.org/wiki/Philosophy",
              "https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F")
openb = ('(', '[', '{')
closeb = (')', ']', '}')


def clear_text(text):
    new_text = []
    counters = [0, 0, 0]
    angle_b = 0
    for symbol in text:
        if symbol == "<":
            angle_b += 1
        if symbol == ">":
            angle_b -= 1
        if angle_b > 0 and all(c == 0 for c in counters):
            new_text.append(symbol)
            continue
        try:
            counters[openb.index(symbol)] += 1
        except ValueError:
            pass
        try:
            counters[closeb.index(symbol)] -= 1
            continue
        except ValueError:
            pass
        if all(c == 0 for c in counters):
            new_text.append(symbol)
    return "".join(new_text)


def get_first_link(soup):
    for content in soup.find_all('div', attrs={'class': 'mw-parser-output'}):
        paragraph = content.find(['p', 'ul'], recursive=False)
        while True:
            if paragraph is not None:
                link = BeautifulSoup(clear_text(str(paragraph)), "lxml").find(is_correct_link)
                paragraph = paragraph.findNext(['p', 'ul'], recursive=False)
                if link is None:
                    continue
                return link
            else:
                break
    return None


def is_correct_link(tag):
    if tag.name is not 'a':
        return False
    if tag.has_attr('class') and (tag['class'] == 'new' or
                                          tag['class'] == 'internal' or
                                          tag['class'] == 'image' or
                                          tag['class'] == 'mw-disambig'):
        return False
    if not tag.has_attr('title'):
        return False
    if tag.parent.name is 'i':
        return False
    if tag.parent.has_attr('id') and tag.parent['id'] == 'coordinates':
        return False
    if tag.has_attr('style') and tag['style'] == 'font-style:italic;':
        return False
    if not tag.has_attr('href') or not tag['href'].startswith('/'):
        return False
    return True


def get_url_parts(url):
    parsed = urlparse(url)
    if not 'wikipedia' in parsed.netloc:
        raise ValueError('not a wiki page')
    return parsed.scheme, parsed.netloc, parsed.path


def main(url):
    scheme, location, path = get_url_parts(url)
    visited_pages = []
    req = get(scheme + '://' + location + path)
    print("Start with:", scheme + '://' + location + path)
    sleep(1)
    while True:
        link = get_first_link(BeautifulSoup(req.text, "lxml"))
        if link is None:
            raise ValueError("No links on that page")
        path = link['href']
        url = scheme + '://' + location + path
        print(link['title'], url)
        if path in visited_pages:
            print("cycle!")
            break
        if url in PHILOSOPHY:
            break
        visited_pages.append(path)
        req = get(url)
        sleep(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " wiki_link")
    else:
        try:
            main(sys.argv[1])
        except ValueError as e:
            print(e)
