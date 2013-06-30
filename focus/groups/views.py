from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from groups.models import Study, StudyForm, Venue, VenueForm, Timeslot, TimeslotForm
from datetime import date, datetime

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
    t = Timeslot.objects.select_related().filter(study_id=study_id)
    print t
    return render_to_response('groups/study.html', {
        'g': g,
        'ts': t,
        'view': 'groups'
    }, context_instance=RequestContext(request))

def edit_study(request, study_id=None, template_name='groups/edit_study.html'):
    # If there is a Study ID, we are editing an existing study and should fetch from DB.
    # Otherwise, make new objects.
    if study_id:
        study = get_object_or_404(Study, pk=study_id)
        timeslots = Timeslot.objects.select_related().filter(study_id=study.id)
    else:
        study = Study()

    # If the data is POSTed, validate and save.
    # Otherwise, we need to prepare the forms to output to the browser.
    if request.POST:
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            # return HttpResponseRedirect(reverse('groups.views.study', kwargs={'study_id': study.id}))
    else:
        form  = StudyForm(instance=study)
        empty_timeslot_form = TimeslotForm(request.POST)


        # If editing, set up the forms for the Study's n Timeslots
        if study_id:
            slots = []
            for i in range(len(timeslots)):
                slot_form = TimeslotForm(instance=timeslots[i])
                slots.append(slot_form)
        else:
            slots = []

    return render_to_response(template_name, {
        'g'          : study,
        'form'       : form,
        'empty_slot' : empty_timeslot_form,
        'slots'      : slots,
        'view'       : 'groups'
    }, context_instance=RequestContext(request))

def create_study(request):
    group_form = StudyForm(request.POST)
    timeslot_form = TimeslotForm(request.POST)
    if request.method == 'POST':
        if group_form.is_valid():
            g = group_form.save()

            for x in range(int(request.POST['timeslot_count'])):
                index = str(x)

                datetime_str = (request.POST['datepicker_'+index]) + " " + (request.POST['timepicker_'+index])
                datetime_obj = datetime.strptime(datetime_str, '%m/%d/%Y %I:%M %p')

                timeslot = Timeslot.objects.create_timeslot(
                    study=g,
                    datetime=datetime_obj,
                    duration=request.POST['duration_'+index],
                    coop_price=request.POST['coop_price_'+index],
                    compensation=request.POST['compensation_'+index],
                    spots=request.POST['spots_'+index]
                )

            print request.POST['timeslot_count']
            return HttpResponseRedirect(reverse('groups.views.study', kwargs={'study_id': g.id}))
        else:
            return render_to_response('groups/edit_study.html', {
                'form': group_form,
                'slot': slot_form,
                'view': 'groups'
            }, context_instance=RequestContext(request))
    else:
        return render_to_response('groups/edit_study.html', {
            'form': group_form,
            'empty_slot': timeslot_form,
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