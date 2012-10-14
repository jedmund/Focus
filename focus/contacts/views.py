from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from contacts.models import Person, PersonForm
from django.http import HttpResponse
from datetime import date

def index(request):
    people_list = Person.objects.all().order_by('last_name')[:5]
    for person in people_list:
        person.age = int((date.today() - person.birthdate).total_seconds()/60/60/24/365)
    t = loader.get_template('contacts/index.html')
    c = Context({
        'people': people_list,
    })
    return HttpResponse(t.render(c))

def person(request, person_id):
    p = get_object_or_404(Person, pk=person_id)

    # Generate the age by subtracting birthdate from today's date
    p.age = int((date.today() - p.birthdate).total_seconds()/60/60/24/365)

    # Determine age from boolean
    p.gender = 'Male' if 1 else 'Female'
    return render_to_response('contacts/person.html', {'p': p})

def edit(request, person_id):
    p = get_object_or_404(Person, pk=person_id)
    form = PersonForm(instance=p)
    return render_to_response('contacts/edit.html', {'p': p, 'form': form})

def create(request):
    form = PersonForm()
    return render_to_response('contacts/edit.html', {'form': form})