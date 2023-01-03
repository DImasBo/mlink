from django.template.response import TemplateResponse
from django.test import TestCase
from django.contrib.sessions.backends.cache import SessionStore

from urllib.parse import urlparse

from magic.manager import ManagerMagicURLSession
from magic.models import MagicURL

from django.test import Client


class MagicURLCreateDetailViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post("/", data={"origin_url": "https://test.org"})

        self.assertEqual(response.status_code, 302)

        id_path = response.url.split("/")[-1]
        self.assertIsNot(id_path, None)

        obj = MagicURL.objects.get(id_path=id_path)
        self.assertEqual(id_path, obj.id_path)

    def test_valid_url(self):
        response: TemplateResponse = self.client.post("/", data={"origin_url": "test.org"})
        form = response.context_data['form']

        self.assertIs(form.is_valid(), False)

