#!/usr/bin/python3
"""Test module for Review class"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from tests.reset_storage import resetStorage


class TestReview(unittest.TestCase):
    """Test suite for class Review"""

    def setup(self):
        """Sets up the test suite"""

        resetStorage()
        pass

    def tearDown(self):
        """Tears down the test suite"""

        resetStorage()
        pass

    # Case 0: Instantiate Review
    def test_9_review_instantiation(self):
        """Tests instantiation of Review class"""

        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(type(review), BaseModel))

    # Case 1: attributes
    def test_9_review_attributes(self):
        """Tests the attributes of the Review instance"""

        review = Review()
        attributes = storage.attributes()["Review"]
        for k, v in attributes.items():
            self.assertTrue(hasattr(review, k))
            self.assertEqual(type(getattr(review, k, None)), v)


if __name__ == "__main__":
    unittest.main()
