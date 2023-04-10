from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template import loader
from .models import Record


def records(request):
    myrecords = Record.objects.all().values()
    template = loader.get_template('all_records.html')
    context = {
        'myrecords': myrecords,
    }
    return HttpResponse(template.render(context, request))


def details1(request, id):
    myrecord = Record.objects.get(id=id)
    print(myrecord.title)
    template = loader.get_template('details.html')
    context = {
        'myrecord': myrecord,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    details_value = ''
    try:
        myrecord = Record.objects.get(id=id)
    except Record.DoesNotExist:
        #raise Http404('Record does not exist')
        return HttpResponseNotFound("No record found")
    if myrecord.title :
        details_value = myrecord.title
    elif myrecord.title == None or myrecord.title == '':
        if myrecord.desc:
            details_value = myrecord.desc
        elif myrecord.desc == None or myrecord.desc == '':
            if myrecord.citablereference:
                details_value = myrecord.citablereference
            else:
                details_value = 'not sufficient information'

    template = loader.get_template('details.html')
    context = {
        'message': details_value,
    }
    return HttpResponse(template.render(context, request))