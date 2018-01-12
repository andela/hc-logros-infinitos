"""Contains tests to check token"""
from django.contrib.auth.hashers import make_password
from hc.test import BaseTestCase


class CheckTokenTestCase(BaseTestCase):
    """Test check token test"""

    def setUp(self):
        super(CheckTokenTestCase, self).setUp()
        self.profile.token = make_password("secret-token")
        self.profile.save()

    def test_it_shows_form(self):
        """Test it shows form"""
        result = self.client.get("/accounts/check_token/alice/secret-token/")
        self.assertContains(result, "You are about to log in")

    def test_it_redirects(self):
        """Test it redirects"""
        result = self.client.post("/accounts/check_token/alice/secret-token/")
        self.assertRedirects(result, "/checks/")

        # After login, token should be blank
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.token, "")

    ### Login and test it redirects already logged in
    def test_redirects_already_loggedin(self):
        """Tests redirects already logged in login"""
        # Login
        self.client.login(username="alice@example.org", password="password")

        # Login again, when already authenticated
        result = self.client.post("/accounts/check_token/alice/secret-token/")
        self.assertRedirects(result, "/checks/")

    ### Login with a bad token and check that it redirects
    def test_it_redirects_bad_token(self):
        """Tests login with  bad token"""
        url = "/accounts/check_token/alice/bad-token/"
        result = self.client.post(url, follow=True)
        self.assertRedirects(result, "/accounts/login/")

    ### Any other tests?
