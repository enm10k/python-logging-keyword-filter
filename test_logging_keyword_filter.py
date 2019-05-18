import logging
from io import StringIO
from unittest import TestCase

from logging_keyword_filter import KeywordFilter


class TestKeywordFilter(TestCase):


    def test_keyword_filter(self):
        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)

        logger = logging.getLogger(__name__)
        logger.addFilter(KeywordFilter('password'))

        password = "P@assw0rd"

        D = {
            'username': 'John Doe',
            'password': password,
        }

        logger.info("%s", D)

        self.assertNotIn(password, log_stream.getvalue())
        self.assertEqual(password, D['password'])