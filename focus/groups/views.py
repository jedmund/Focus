from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from groups.models import Study, StudyForm, Venue, VenueForm
from datetime import date

def index(request):
    studies = Study.objects.all().order_by('topic')[:5]
    t = loader.get_template('groups/index.html')
    c = Context({
        'studies': studies,
        'view': 'groups'
    })
    return HttpResponse(t.render(c))

def study(request, study_id):
    g = get_object_or_404(Study, pk=study_id)
    return render_to_response('groups/study.html', {
        'g': g,
        'view': 'groups'
    }, context_instance=RequestContext(request))

def edit_study(request, study_id):
    return HttpResponse("Edit this study.")

def create_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            g = form.save()
            return HttpResponseRedirect(reverse('groups.views.study', kwargs={'study_id': g.id}))
        else:
            return render_to_response('groups/edit_study.html', {
                'form': form,
                'view': 'groups'
            }, context_instance=RequestContext(request))
    else:
        form = StudyForm()
        return render_to_response('groups/edit_study.html', {
            'form': form,
            'view': 'groups'
        }, context_instance=RequestContext(request))

def venues(request):
    venues = Venue.objects.all().order_by('name')[:5]
    t = loader.get_template('groups/venues.html')
    c = Context({
        'venues': venues,
        'view': 'venues',
    })
    return HttpResponse(t.render(c))


def venue(request, venue_id):
    v = get_object_or_404(Venue, pk=venue_id)
    return render_to_response('groups/venue.html', {
        'v': v,
        'view': 'venues'
    }, context_instance=RequestContext(request))


def edit_venue(request, venue_id):
    v = get_object_or_404(Venue, pk=venue_id)
    form = VenueForm(instance=v)
    return render_to_response('groups/edit_venue.html', {'v': v, 'form': form, 'view': 'v'})

def create_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            v = form.save()
            return HttpResponseRedirect(reverse('groups.views.venue', kwargs={'venue_id': v.id}))
        else:
            return render_to_response('groups/edit_venue.html', {
                'form': form,
                'view': 'venues'
            }, context_instance=RequestContext(request))
    else:
        form = VenueForm()
        return render_to_response('groups/edit_venue.html', {
            'form': form,
            'view': 'venues'
        }, context_instance=RequestContext(request))