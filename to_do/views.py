
from django.shortcuts import render_to_response#, redirect
from django.template import RequestContext

from to_do.forms import TaskForm, SignUpForm, LogInForm
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

    tasks = Task.objects.all().order_by('completed')

    form = TaskForm()
    ctx = {
        'form': form,
        'tasks': tasks
    }
    ctx = RequestContext(request, ctx)
    response = render_to_response(template, ctx)

    return response