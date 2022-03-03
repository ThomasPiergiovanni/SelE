"""Test add voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from vote.views.create_voting import CreateVoting


class TestCreateVoting(TestCase):
    """Test CreateVoting view class.
    """
    def setUp(self):
        self.view = CreateVoting()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_get_success_template(self):
        self.assertEqual(
            self.view.get_success_template,'vote/create_voting.html'
        )

    def test_init_with_attr_post_success_template(self):
        self.assertEqual(
            self.view.post_success_template, 'vote:overview'
        )

    def test_init_with_attr_post_fail_template(self):
        self.assertEqual(
            self.view.post_fail_template, 'vote:create_voting'
        )
