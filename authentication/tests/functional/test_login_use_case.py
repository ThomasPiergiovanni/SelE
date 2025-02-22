# pylint: disable=C0114,C0115,C0116,E1101,R0201
import os
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class LoginUseCaseTest(StaticLiveServerTestCase):

    def setUp(self):
        firefox_options = webdriver.FirefoxOptions()
        if os.name == 'nt':
            firefox_options.headless = False
            self.browser = webdriver.Firefox(
                executable_path=str(
                    r'D:\projects\sele\config\settings\geckodriver.exe'
                ),
                options=firefox_options,
            )
        if os.name == 'posix':
            firefox_options.headless = True
            self.browser = webdriver.Firefox(
                executable_path=str('/usr/local/bin/geckodriver'),
                options=firefox_options,
            )
        self.browser.implicitly_wait(30)
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()

    def tearDown(self):
        self.browser.quit()

    def test_vote_use_case(self):
        # The user is on the home page.
        self.browser.get(f"{self.live_server_url}{''}")
        sleep(2)
        self.assertIn(
            'sel-e',
            self.browser.find_element_by_tag_name('h1').text
        )

        # The user selects the connexion button.
        sleep(2)
        self.browser.find_element_by_id('go_to_login_button').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_class_name('login-box-msg').text,
            "Connectez-vous à votre compte"
        )

        # The user types its email password clicks and then clicks
        # "Se connecter" button and lands on the home page.
        sleep(2)
        self.browser.find_element_by_id('input_login_email')\
            .send_keys('user1@email.com')
        sleep(2)
        self.browser.find_element_by_id('input_login_password')\
            .send_keys('xxx_Xxxx')
        sleep(2)
        self.browser.find_element_by_id('login_button').click()
        self.assertIn(
            'sel-e',
            self.browser.find_element_by_tag_name('h1').text
        )
        sleep(2)
