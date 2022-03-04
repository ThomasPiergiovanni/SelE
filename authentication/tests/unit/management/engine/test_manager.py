"""Test manager module.
"""
from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.management.engine.manager import Manager
from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from collectivity.models.collectivity import Collectivity
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)

class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        CollectivityEmulation().emulate_postal_code()
        CollectivityEmulation().emulate_collectivity()
        CollectivityEmulation().emulate_set_collectivity_postal_code()
        self.manager = Manager()
    
    def test_check_collectivity_with_valid_form_data(self):
        method_result = self.manager.check_collectivity(
            '92220',
            'Bagneux'
        )
        self.assertIsInstance(method_result, Collectivity)

    def test_check_collectivity_with_invalid_form_data(self):
        method_result = self.manager.check_collectivity(
            '92220',
            'Bourg-la-Reine'
        )
        self.assertFalse(method_result)

    def test_create_cu_with_valid_form_and_cu_instance(self):
        form = AuthenticationEmulation().emulate_custom_user_form()
        form.is_valid()
        collectivity = Collectivity.objects.all().last()
        self.manager.create_custom_user(form, collectivity)
        self.assertEqual(
            CustomUser.objects.all().last().email,
            'user@email.com'
        )
    
    def test_activate_collectivity(self):
        collectivity = Collectivity.objects.get(name__exact='Bagneux')
        self.assertEqual(collectivity.activity, 'no')
        self.manager.activate_collectivity(collectivity)
        self.assertEqual(collectivity.activity, 'yes')

    def test_edit_cu_with_valid_form_and_cu_instance(self):
        # form = AuthenticationEmulation().emulate_edit_custom_user_form()
        # form.is_valid()
        # request = RequestFactory().post('')
        # session_middleware = SessionMiddleware(get_response=request)
        # session_middleware.process_request(request)
        # user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        # collectivity = Collectivity.objects.get(
        #     pk=user.collectivity
        # )
        # self.manager.edit_custom_user(request, form, collectivity)
        # self.assertEqual(
        #     CustomUser.objects.all().last().user_name,
        #     'UserNameNew'
        # )
