from records.models import Record
from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='Indicates the id to be created')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        api_endpoint ='http://discovery.nationalarchives.gov.uk/API/records/v1/details/'
        response =requests.get(api_endpoint + id)
        status_code=response.status_code
        if status_code ==200:
            res = response.json()
            title =res["title"]
            desc=res["scopeContent"]["description"]
            citablereference=res["citableReference"]
            print(title)
            print(desc)
            record = Record(id=id, title=title,desc=desc,citablereference=citablereference)
            record.save()
            return 'Record saved'
        else:
            #raise Exception('Record for ID  "%s" does not exist' % id)
            print('Record for ID  "%s" does not exist' % id)
            return 'Record for ID  %s does not exist' % id