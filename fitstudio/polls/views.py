from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm

def schedule(request):
    template = loader.get_template('polls/schedule.html')
    return render(request, 'polls/schedule.html')

def index(request):
    template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
            'is_taken': User.objects.filter(username_iexact=username).exists()
            }
    return JsonResponse(data)

