from io import StringIO

from django.core.management import call_command
from django.test import  TestCase
from records.models import Record
#from records.management.commands.add_id import Command


class CommandsTestCase(TestCase):
    def test_command_output_with_valid_id (self):
        out = StringIO()
        result = call_command('add_id','a147aa58-38c5-45fb-a340-4a348efa01e6', stdout=out)
        record =Record.objects.get(id='a147aa58-38c5-45fb-a340-4a348efa01e6')
        self.assertTrue(record != None)
        self.assertIn('Record saved', out.getvalue())

    def test_command_output_with_invalid_id(self):
        out = StringIO()
        result = call_command('add_id', '1', stdout=out)
        self.assertIn('Record for ID  1 does not exist', out.getvalue())
