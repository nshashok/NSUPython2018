from time import sleep
from urllib.request import url2pathname

import requests
from bs4 import BeautifulSoup as Soup, NavigableString
import sys


eng_url_prefix = 'https://en.wikipedia.org'
ru_url_prefix = 'https://ru.wikipedia.org'

eng_target_url = 'https://en.wikipedia.org/wiki/Philosophy'
ru_target_url = 'https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F'
random_eng_page_url = 'https://en.wikipedia.org/wiki/Special:Random'
random_ru_page_url = 'https://ru.wikipedia.org/wiki/Special:Random'


def print_err(*values, sep='\n'):
    print(*values, sep=sep, file=sys.stderr)


ANCHOR_TAG_NAME = 'a'
BRACKET = 'bracket'

invalid_markers_counters = dict()

invalid_classes = {
    'thumb',
    'hatnote',
    'navigation-not-searchable',
    'infobox',
    'mw-editsection',
    'noprint',
    'toc',
    'selflink',
    'mw-disambig',
    'dablink',
    'references-wrap',
    'mw-headline',
    'reference',
    'thumbinner',
    'metadata',
}

invalid_tags = {
    'table',
    'noscript',
    'i',
    'sub',
    'sup'
}


def download_web_content(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise RuntimeError("Failed to fetch content from {}".format(url))


bracket_counter = 0

def inc(dictionary, key):
    dictionary[key] = dictionary.get(key, 0) + 1


def dec(dictionary, key):
    dictionary[key] = max(dictionary.get(key, 0) - 1, 0)


def get_tag_classes(tag):
    try:
        return tag['class']
    except:
        return []


def maybe_get_next_url(child):

    def _search_for_invalid_markers(string):
        for char in string:
            if char == '(':
                inc(invalid_markers_counters, BRACKET)
            elif char == ')':
                dec(invalid_markers_counters, BRACKET)

    if type(child) == NavigableString:
        _search_for_invalid_markers(child)
        return None

    if child.name in invalid_tags or any(v in invalid_classes for v in get_tag_classes(child)):
        return None

    if child.name == ANCHOR_TAG_NAME:
        href = child['href']
        if 'new' not in get_tag_classes(child) and invalid_markers_counters.get(BRACKET, 0) == 0:
            return href
        else:
            return None
    else:
        maybe_url = None
        for c in child.children:
            maybe_url = maybe_get_next_url(c)
            if maybe_url is not None:
                break
        return maybe_url


def main(start_url: str):
    url = start_url
    visited_urls = set()

    while True:
        print(url2pathname(url))
        if url == eng_target_url or url == ru_target_url:
            print("Reached philosophy page")
            break

        if url in visited_urls:
            print("Cycle has been found")
            break

        visited_urls.add(url)

        response_text = download_web_content(url)
        soup = Soup(response_text, 'lxml')
        content_body = soup.select("#mw-content-text")[0]

        maybe_url = maybe_get_next_url(content_body)

        if maybe_url is None:
            print('No valid url has been found')
            break

        if url.startswith(eng_url_prefix):
            url = eng_url_prefix + maybe_url
        else:
            url = ru_url_prefix + maybe_url
        sleep(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        start_url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BC%D0%BE%D0%BB%D1%91%D1%82"
        main(random_eng_page_url)
