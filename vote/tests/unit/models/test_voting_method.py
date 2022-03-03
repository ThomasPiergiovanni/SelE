"""Test voting method module.
"""
from django.db import models
from django.test import TestCase

from vote.models.voting_method import VotingMethod


class VotingMethodTest(TestCase):
    """Test voting method class.
    """
    def setUp(self):
        self.emulate_voting_method()

    def emulate_voting_method(self):
        """
        """
        VotingMethod.objects.create(id=1, name="Majoritaire", percentage=0.5)
        VotingMethod.objects.create(id=2, name="Consensus75",  percentage=0.75)

    def test_voting_methods_with_status_class(self):
        voting_method = VotingMethod.objects.get(pk=1)
        self.assertIsInstance(voting_method, VotingMethod)

    def test_voting_method_with_attr_name_characteristic(self):
        attribute = VotingMethod._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)

    def test_voting_method_with_attr_percentage_characteristic(self):
        attribute = VotingMethod._meta.get_field('percentage')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DecimalField()))
        self.assertEqual(attribute.validators[0].limit_value, 0.01)
        self.assertEqual(attribute.validators[1].limit_value, 1)
        self.assertEqual(attribute.max_digits, 3)
        self.assertEqual(attribute.decimal_places, 2)
    
    def test_voting_method_with_emulated_voting_method_instance(self):
        voting_method = VotingMethod.objects.get(pk=1)
        self.assertEqual(voting_method.name, "Majoritaire")
        self.assertEqual(voting_method.percentage, 0.5)
        voting_method = VotingMethod.objects.get(pk=2)
        self.assertEqual(voting_method.name, "Consensus75")
        self.assertEqual(voting_method.percentage, 0.75)