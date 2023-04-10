from django.test import TestCase

from records.models import Record

class RecordModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Record.objects.create(id='1',title='test_title', desc='test_desc',citablereference='test_citablereference')

    def test_record(self):
        record = Record.objects.get(id=1)
        self.assertEqual(record.title, 'test_title')

    def test_title_label(self):
        record = Record.objects.get(id=1)
        field_label = record._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_desc_max_length(self):
        record = Record.objects.get(id=1)
        max_length = record._meta.get_field('desc').max_length
        self.assertEqual(max_length, 255)

