from argparse import ArgumentParser
from sys import stderr
from time import time, sleep, ctime
from typing import Iterable
from urllib import request
from urllib.parse import urljoin
from urllib.request import url2pathname, pathname2url

from bs4 import BeautifulSoup, NavigableString, Tag

PHILOSOPHY_PAGES = (
    'https://en.wikipedia.org/wiki/Philosophy',
    urljoin('https://ru.wikipedia.org/wiki/', pathname2url('Философия')),
)


def count_parentheses(text: str, parentheses: Iterable[str]=None):
    if parentheses is None:
        parentheses = (
            ('(', '[', '{'),
            (')', ']', '}'),
        )
    counter = [0] * len(parentheses[0])
    for char in text:
        try:
            open_idx = parentheses[0].index(char)
        except ValueError:
            try:
                close_idx = parentheses[1].index(char)
            except ValueError:
                pass
            else:
                counter[close_idx] -= 1
        else:
            counter[open_idx] += 1
    return counter


def in_parentheses(tag: Tag) -> bool:
    all_text_before = "".join(text for text in tag.previous_siblings
                              if isinstance(text, NavigableString))
    all_text_after = "".join(text for text in tag.next_siblings
                             if isinstance(text, NavigableString))
    return any(
        open_counter > 0 > close_counter
        for open_counter, close_counter in zip(
            count_parentheses(all_text_before),
            count_parentheses(all_text_after)
        )
    )


EXCLUDED_LINK_CLASSES = {
    'new',
    'mw-disambig',
    'image',
}


def is_a_good_link(tag: Tag) -> bool:
    return (
        tag.name == 'a' and
        tag.has_attr('href') and
        tag['href'].startswith('/') and
        tag.has_attr('title') and
        not (
            tag.has_attr('class') and
            EXCLUDED_LINK_CLASSES.intersection(tag['class']) or
            in_parentheses(tag)
        )
    )


EXCLUDED_PARENTS = {
    'i',
    'sup'
}

EXCLUDED_CLASSES = {
    'infobox',
    'vertical-navbox',
    'toc',
    'references-wrap',
    'mw-headline',
    'mw-editsection',
    'reference',
    'dablink',
    'thumbinner',
    'metadata',
    'hatnote',
    'navigation-not-searchable',
}


def is_a_bad_tag(tag: Tag) -> bool:
    return (
        tag.name in EXCLUDED_PARENTS or
        tag.has_attr('class') and EXCLUDED_CLASSES.intersection(tag['class'])
    )


def find_lazy(content, *args, **kwargs):
    result = content.find(*args, **kwargs)
    while result is not None:
        yield result
        result = result.find_next(*args, **kwargs)


def good_link_parents(root: Tag):
    tag = root

    while tag:
        if tag.name == 'a':
            yield tag.parent
            tag = tag.find_next()
        elif is_a_bad_tag(tag):
            tag = tag.find_next_sibling() or tag.parent.find_next_sibling()
        else:
            tag = tag.find_next()


def first_good_link(wiki_page):
    soup = BeautifulSoup(
        wiki_page, 'html.parser')
    root = soup.find(attrs={'class': 'mw-parser-output'})
    for parent in good_link_parents(root.find()):
        try:
            first_url = next(find_lazy(parent, is_a_good_link))
            break
        except StopIteration:
            pass
    else:
        return None

    return first_url['href']


def main(url: str, time_between_requests: float):
    visited = set()
    last_request_time = 0

    def calc_time_to_sleep():
        return time_between_requests - (time() - last_request_time)

    while url not in visited:
        visited.add(url)

        if url in PHILOSOPHY_PAGES:
            break

        time_to_sleep = calc_time_to_sleep()
        while time_to_sleep > 0:
            sleep(time_to_sleep)
            time_to_sleep = calc_time_to_sleep()
        last_request_time = time()

        with request.urlopen(url) as wiki_page:
            path = first_good_link(wiki_page)
            if path is None:
                break
            print(ctime(), '--', urljoin(url, url2pathname(path)))
            url = urljoin(url, path)
    else:
        print('cycle :(', file=stderr)


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.description = """Checks whether a specified Wikipedia page leads
    to some philosophical page by walking recursively through the first link at 
    each page"""
    arg_parser.add_argument('url', help='wiki page to check')
    arg_parser.add_argument('time_between_requests', nargs='?', default=0.5)
    ns = arg_parser.parse_args()
    main(ns.url, ns.time_between_requests)
