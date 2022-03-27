"""Collectivity Voting Form module 
"""
from django.forms import ChoiceField, Form, Select


class CollectivityVotingsForm(Form):
    """CollectivityVotingsForm class. Used for sorting collectivity votings
    page objects.
    """
    attribute_selector = ChoiceField(
        label='Trier par:',
        choices=(('question', 'Question'), ('date', 'Date de création')),
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_attribute_selector',
                'autofocus': False,
            }
        )
    )

    order_selector = ChoiceField(
        label='Dans l\'ordre:',
        choices=(('asc', 'Ascendant'), ('desc', 'Descendant')),
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_order_selector',
                'autofocus': False,
            }
        )
    )
