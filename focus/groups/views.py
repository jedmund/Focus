from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from groups.models import Study, Venue
from datetime import date

def index(request):
    studies = Study.objects.all().order_by('topic')[:5]
    t = loader.get_template('groups/index.html')
    c = Context({
        'studies': studies,
    })
    return HttpResponse(t.render(c))
