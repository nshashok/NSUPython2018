from os import listdir
import os.path
from unittest import TestCase, main
from urllib import request
from urllib.parse import urljoin
from urllib.request import pathname2url, url2pathname

from bs4 import BeautifulSoup

from problem1.wiki_page_leads_to_philosophy import is_a_good_link, \
    first_good_link


class Test(TestCase):
    test_examples_dir = os.path.join(os.path.dirname(__file__), 'test_examples')
    good_link_blocks_dir = os.path.join(test_examples_dir, 'good_link_blocks')
    bad_link_blocks_dir = os.path.join(test_examples_dir, 'bad_link_blocks')
    first_good_link_examples = {
        'https://en.wikipedia.org/wiki/1938_in_film': '/wiki/MGM',
        'https://en.wikipedia.org/wiki/American_football':
            '/wiki/Offense_(sports)',
        urljoin('https://ru.wikipedia.org/wiki/', pathname2url('ВМ-Т')):
            pathname2url('/wiki/Опытное_конструкторское_бюро'),
        urljoin('https://ru.wikipedia.org/wiki/', pathname2url('Философия')):
            pathname2url('/wiki/Познание'),
        urljoin('https://ru.wikipedia.org/wiki/', pathname2url('Головной_убор')):
            pathname2url('/wiki/Причёска'),

    }

    def test_is_a_good_link_on_good_links(self):
        for test_file_name in listdir(self.good_link_blocks_dir):
            with open(os.path.join(self.good_link_blocks_dir,
                                   test_file_name)) as fp:
                content = BeautifulSoup(fp, 'html.parser')
                for a in content.find_all('a'):
                    self.assertTrue(is_a_good_link(a), test_file_name)

    def test_is_a_good_link_on_bad_links(self):
        for test_file_name in listdir(self.bad_link_blocks_dir):
            with open(os.path.join(self.bad_link_blocks_dir,
                                   test_file_name)) as fp:
                for a in BeautifulSoup(fp, 'html.parser').find_all('a'):
                    self.assertFalse(is_a_good_link(a), test_file_name)

    def test_first_good_link(self):
        for url, correct_link in \
                self.first_good_link_examples.items():
            with request.urlopen(url) as wiki_page:
                link = first_good_link(wiki_page)
                self.assertEqual(correct_link, link, '%s != %s' % (
                    url2pathname(correct_link), url2pathname(link)))


if __name__ == '__main__':
    main()
