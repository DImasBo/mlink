from django.template.response import TemplateResponse
from django.test import TestCase
from magic.models import MagicURL

from django.test import Client


class MagicURLModelViewTestCase(TestCase):

    def test_create(self):
        obj = MagicURL(origin_url="https://test.org")
        obj.save()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.id_path)


class MagicURLRedirectViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_obj = MagicURL(origin_url="https://google.com")
        self.test_obj.save()

    def test_check_redirect(self):
        response = self.client.get(self.test_obj.get_url_by_id_path())

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.test_obj.origin_url)


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

    def test_not_valid_url(self):
        response: TemplateResponse = self.client.post("/", data={"origin_url": "test.org"})
        form = response.context_data['form']

        self.assertIs(form.is_valid(), False)

    def test_replace_url(self):
        # create first link
        response = self.client.post("/", data={"origin_url": "https://test.org"})
        self.assertEqual(response.status_code, 302)

        # create second again
        response2 = self.client.post("/", data={"origin_url": "https://test.org"})
        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, response2.url)
