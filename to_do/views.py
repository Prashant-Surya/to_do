
from django.shortcuts import render_to_response
from django.template import RequestContext

from to_do.forms import SignUpForm, TaskForm, LogInForm

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
    form = TaskForm()
    ctx = {
        'form': form
    }
    ctx = RequestContext(request, ctx)
    response = render_to_response(template, ctx)

    return response