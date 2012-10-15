from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from contacts.models import Person, PersonForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date

def index(request):
    people = Person.objects.all().order_by('last_name')
    for person in people:
        person.age = int((date.today() - person.birthdate).total_seconds()/60/60/24/365)

    paginator = Paginator(people, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    t = loader.get_template('contacts/index.html')
    c = Context({
        'people': contacts,
        'view': 'contacts'
    })
    return HttpResponse(t.render(c))

def person(request, person_id):
    p = get_object_or_404(Person, pk=person_id)

    # Generate the age by subtracting birthdate from today's date
    p.age = int((date.today() - p.birthdate).total_seconds()/60/60/24/365)

    # Determine age from boolean
    p.gender = 'Male' if 1 else 'Female'
    return render_to_response('contacts/person.html', {'p': p, 'view': 'contacts'})

def edit(request, person_id):
    p = get_object_or_404(Person, pk=person_id)
    form = PersonForm(instance=p)
    return render_to_response('contacts/edit.html', {'p': p, 'form': form, 'view': 'contacts'})

def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            p = form.save()
            print p.id
            return HttpResponseRedirect(reverse('contacts.views.person', kwargs={'person_id': p.id}))
        else:
            print form
            return render_to_response('contacts/edit.html', {
                'form': form,
                'view': 'contacts'
            }, context_instance=RequestContext(request))
    else:
        form = PersonForm()
        return render_to_response('contacts/edit.html', {
            'form': form,
            'view': 'contacts'
        }, context_instance=RequestContext(request))