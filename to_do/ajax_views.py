import json

from django.http import HttpResponse

from to_do.models import Task


def save_new_form(request):
    text = request.POST["text"]

    kwargs = {
        'text': text
    }

    Task.objects.create(**kwargs)

    print request.POST

    result = {
        'status': "OK",
        'status_code': 200
    }

    return HttpResponse(
        json.dumps(
            result, indent=4),
        mimetype='application/json')
