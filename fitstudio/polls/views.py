from django.shortcuts import render
import logging

# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

logger = logging.getLogger(__name__)

class SignUpView(CreateView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm

def schedule(request):
    template = loader.get_template('polls/schedule.html')
    return render(request, 'polls/schedule.html')

def index(request):
    template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
            'is_taken': User.objects.filter(username_iexact=username).exists()
            }
    return JsonResponse(data)

def get_events(request):
    date = request.GET.get('date', None)
    logger.error('========= date:' + date)

    data = {
        'locale': 'pl',
        'defaultView': 'agendaDay',
        'defaultDate': 'date',
        'header': {
            'left': 'prev,next today',
            'center': 'Plan zajęć',
            'right': 'month,agendaWeek,agendaDay'
        },
        'editable': 'false',
        'events': [
            {
                'title': 'Salsa',
                'color': 'yellow',
                'textColor': 'black',
                'start': '2018-01-16T17:15:00Z',
                'end': '2018-01-16T18:30:00Z'
            }
        ]
    }

    return JsonResponse(data)
