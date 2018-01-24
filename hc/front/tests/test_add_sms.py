import json
from hc.api.models import Channel
from hc.test import BaseTestCase


class AddSMSTestCase(BaseTestCase):

    def test_sms_works(self):
        self.client.login(username="alice@example.org", password="password")
        r = self.client.get("/integrations/add_sms/")
        self.assertContains(r, "Integration Settings", status_code=200)