from django.test import TestCase

from records.models import Record
from records.views import records,details
from django.urls import reverse

class RecordViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Record.objects.create(id='1',title='test_title', desc='test_desc',citablereference='test_citablereference')

    def test_view_url_records(self):
        response = self.client.get('/records/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_records(self):
        response = self.client.get(reverse('records'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_details(self):
        response = self.client.get('/records/details/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_details(self):
        record = Record.objects.get(id=1)
        response = self.client.get(reverse('details',args=record.id))
        self.assertEqual(response.status_code, 200)

    def test_view_records_uses_correct_template(self):
        response = self.client.get(reverse('records'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_records.html')

    def test_view_details_uses_correct_template(self):
        record = Record.objects.get(id=1)
        response = self.client.get(reverse('details', args=record.id))
        self.assertTemplateUsed(response, 'details.html')
