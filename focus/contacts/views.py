from contacts.models import Person
from django.http import HttpResponse

def index(request):
    people_list = Poll.objects.all().order_by('-last_name')[:5]
    output = ', '.join([p.first_name for p in people_list])
    return HttpResponse(output)

def person(request):
    return HttpResponse("This is a person.")

def create(request):
    return HttpResponse("Add a new person.")

def edit(request):
    return HttpResponse("Edit this person.")