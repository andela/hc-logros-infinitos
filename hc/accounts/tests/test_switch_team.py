"""Test switch team"""
from hc.test import BaseTestCase
from hc.api.models import Check


class SwitchTeamTestCase(BaseTestCase):
    """Test cases switch to teams"""

    def test_it_switches(self):
        """Test check switches"""
        check = Check(user=self.alice, name="This belongs to Alice")
        check.save()

        self.client.login(username="bob@example.org", password="password")

        url = "/accounts/switch_team/%s/" % self.alice.username
        result = self.client.get(url, follow=True)

        ### Assert the contents of r
        self.assertContains(result, "alice")


    def test_it_checks_team_membership(self):
        """Tests it checks team membership"""
        self.client.login(username="charlie@example.org", password="password")

        url = "/accounts/switch_team/%s/" % self.alice.username
        result = self.client.get(url)
        ### Assert the expected error code
        self.assertEqual(result.status_code, 403)

    def test_it_switches_to_own_team(self):
        """Tests that it switches teams"""
        self.client.login(username="alice@example.org", password="password")

        url = "/accounts/switch_team/%s/" % self.alice.username
        result = self.client.get(url, follow=True)
        ### Assert the expected error code
        self.assertEqual(result.status_code, 200)
