import unittest
from unittest.mock import patch

from lecture import randomised_function


class MyTestCase(unittest.TestCase):
    def test_randomised_function(self):
        with patch("random.randint", return_value=3):
            self.assertEqual('software', randomised_function())

        with patch("random.randint", return_value=8):
            self.assertEqual('engineering', randomised_function())
