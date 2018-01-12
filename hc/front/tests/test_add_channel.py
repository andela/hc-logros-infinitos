from django.test.utils import override_settings
from django.contrib.auth.models import User

from hc.api.models import Channel
from hc.test import BaseTestCase


@override_settings(PUSHOVER_API_TOKEN="token", PUSHOVER_SUBSCRIPTION_URL="url")
class AddChannelTestCase(BaseTestCase):

    def test_it_adds_email(self):
        url = "/integrations/add/"
        form = {"kind": "email", "value": "alice@example.org"}

        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url, form)

        self.assertRedirects(r, "/integrations/")
        assert Channel.objects.count() == 1

    def test_it_trims_whitespace(self):
        """ Leading and trailing whitespace should get trimmed. """

        url = "/integrations/add/"
        form = {"kind": "email", "value": "   alice@example.org   "}

        self.client.login(username="alice@example.org", password="password")
        self.client.post(url, form)

        q = Channel.objects.filter(value="alice@example.org")
        self.assertEqual(q.count(), 1)

    def test_instructions_work(self):
        self.client.login(username="alice@example.org", password="password")
        kinds = ("email", "webhook", "pd", "pushover", "hipchat", "victorops")
        for frag in kinds:
            url = "/integrations/add_%s/" % frag
            r = self.client.get(url)
            self.assertContains(r, "Integration Settings", status_code=200)

    ### Test that the team access works
    def test_team_access_channel_works(self):
        alice = User.objects.get(email="alice@example.org")
        self.client.login(username="bob@example.org", password="password")
        url ="/integrations/add/"
        form = {"kind": "email", "value":"bob@example.org"}
        r = self.client.post(url, form)
        self.client.logout()
        self.client.login(username="alice@example.org", password="password")
        q = Channel.objects.filter(user= alice, value="bob@example.org")
        self.assertEqual(q.count(), 1)        
        self.assertEqual(r.status_code, 302)


    ### Test that bad kinds don't work
    def test_bad_kinds_dont_work(self):
        """Test that an improper integration can not be added"""

        url = "/integrations/add/"
        form = {"kind": "whatsapp", "value": "alice@example.org"}

        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url, form)
        self.assertEqual(r.status_code, 400)

        q = Channel.objects.filter(value="alice@example.org")
        self.assertEqual(q.count(), 0)
