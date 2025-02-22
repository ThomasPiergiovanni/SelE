# pylint: disable=C0114,C0115,C0116,E1101,R0801
import os
from datetime import date, timedelta
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.tests.emulation.vote_emulation import VoteEmulation


class CreateVotingUseCaseTest(StaticLiveServerTestCase):

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
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()

    def tearDown(self):
        self.browser.quit()

    def tests_create_voting_use_case(self):
        # The user is on the login page
        self.browser.get(f"{self.live_server_url}{'/authentication/login/'}")

        # The user types its email, password and then clicks
        # "Se connecter" button. The user lands on the home page.
        sleep(2)
        self.browser.find_element_by_id('input_login_email')\
            .send_keys('user1@email.com')
        sleep(2)
        self.browser.find_element_by_id('input_login_password')\
            .send_keys('xxx_Xxxx')
        sleep(2)
        self.browser.find_element_by_id('login_button').click()
        sleep(2)
        self.assertIn(
            'sel-e',
            self.browser.find_element_by_tag_name('h1').text
        )
        sleep(2)

        # The user selects "Mon groupe Local" on the left navigation sidebar
        # and the selects "Votes"
        self.browser.find_element_by_id('sidebar_my_local_group').click()
        sleep(2)
        self.browser.find_element_by_id('sidebar_mlg_votings').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'Votations - Bourg-la-Reine (92340)',
        )
        sleep(2)

        # The user selects the "Créer une votation" button
        self.browser.find_element_by_id('go_to_create_voting_button').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'Votation - Créer',
        )
        sleep(2)

        # The user fills the form and selects the "créer" button. The user
        # should land on the votings page and see its created voting
        # on the top of the list.
        self.browser.find_element_by_id('input_voting_question')\
            .send_keys('Voulez-vous améliorer sel-e?')
        sleep(2)
        self.browser.find_element_by_id('input_voting_description')\
            .send_keys('bla bla bla')
        sleep(2)
        self.browser.find_element_by_id('input_voting_voting_method')\
            .send_keys('Majoritaire')
        sleep(2)
        today = date.today()
        self.browser.find_element_by_id('input_voting_opening_date')\
            .send_keys(str(today))
        sleep(2)
        self.browser.find_element_by_id('input_voting_closure_date')\
            .send_keys(str(today + timedelta(days=5)))
        sleep(2)
        self.browser.find_element_by_id('create_voting_button').click()
        self.assertTrue(self.browser.find_element_by_tag_name('td'))
        sleep(2)
