import json

from django.http import HttpResponse

from to_do.models import Task


def save_new_form(request):
    text = request.POST["text"]

    kwargs = {
        'text': text
    }

    t = Task.objects.create(**kwargs)

    print request.POST

    result = {
        'status': "OK",
        'id': int(t.id),
        'text': text,
    }

    return HttpResponse(
        json.dumps(
            result, indent=4),
        mimetype='application/json')


def update_task(request):
    task_id = request.POST["id"]
    task_text = request.POST.get("task_text", None)
    task_completed = request.POST.get("completed", False)

    t = Task.objects.get(id=task_id)

    if task_text:
        t.text = task_text

    if task_completed != False:
        if task_completed == "true":
            t.completed = True
        elif task_completed == "false":
            t.completed = False

    t.save()

    result = {
        'status': "OK"
    }

    return HttpResponse(
        json.dumps(
            result, indent=4),
        mimetype='application/json')


def delete_task(request):
    task_id = request.POST['id']
    t = Task.objects.get(id=task_id)

    t.delete()

    result = {
        'status': "OK"
    }

    return HttpResponse(
        json.dumps(
            result, indent=4),
        mimetype='application/json')
