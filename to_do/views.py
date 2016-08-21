
from django.shortcuts import render_to_response
from django.template import RequestContext

from to_do.forms import SignUpForm, TaskForm, LogInForm
from to_do.models import Task


def home(request):
    template = 'login.html'

    signup_form = SignUpForm()
    login_form = LogInForm()
    ctx = {
        'signup_form': signup_form,
        'login_form': login_form,
    }
    ctx = RequestContext(request, ctx)
    response = render_to_response(template, ctx)

    return response


def lists(request):
    template = 'lists.html'
    tasks = Task.objects.filter(completed=False)
    t = []
    for i in tasks:
        k = {
            'id': int(i.id),
            'text': str(i.text)
        }
        t.append(k)
    form = TaskForm()
    ctx = {
        'form': form,
        'tasks': t
    }
    ctx = RequestContext(request, ctx)
    response = render_to_response(template, ctx)

    return response