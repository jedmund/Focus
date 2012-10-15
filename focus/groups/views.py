from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from groups.models import Study, StudyForm, Venue, VenueForm
from datetime import date

def index(request):
    studies = Study.objects.all().order_by('topic')[:5]
    t = loader.get_template('groups/index.html')
    c = Context({
        'studies': studies,
    })
    return HttpResponse(t.render(c))

def study(request):
    return HttpResponse("This is a study.")

def edit_study(request, study_id):
    return HttpResponse("Edit this study.")

def create_study(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = StudyForm()
        return render_to_response('groups/edit_study.html', {'form': form, 'view': 'groups'})

def venue(request):
    return HttpResposne("This is a venue.")

def edit_venue(request):
    return HttpResponse("Edit this venue.")

def create_venue(request):
    return HttpResponse("Create a venue.")