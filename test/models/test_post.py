from unittest import TestCase
from app.models.post import Post
from . import fixtures


class TestPost(TestCase):
    def test_post_initializes_properly(self):
        p = Post(fixtures.Post.post_metadata)
        self.assertDictEqual(fixtures.Post.post_metadata, p.__dict__)
