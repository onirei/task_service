from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .forms import CreateTask
from .models import Task


#отображение всех записей, пангинация
def task_list(request):
    order = request.GET.get('order_by')
    if not order:
        order = 'id'
    tasks_list = Task.objects.all().order_by(order)
    paginator = Paginator(tasks_list, 10)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return render_to_response('task_list.html', {'tasks': tasks, 'order': order})

#отображение одной записи
def task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    return render(request, 'task.html', {'task': task_obj})

#удаление записи
def del_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.delete()
    return HttpResponseRedirect('/task_list')

#изменение записи
def change_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if request.POST:
        chn_task = CreateTask(request.POST, request.FILES)
        if chn_task.is_valid():
            task_obj.name = chn_task.cleaned_data['name']
            task_obj.about = chn_task.cleaned_data['about']
            if chn_task.cleaned_data['image']:
                task_obj.image = chn_task.cleaned_data['image']
            task_obj.expiration_date = chn_task.cleaned_data['expiration_date']
            task_obj.status = chn_task.cleaned_data['status']
            task_obj.save()
            return HttpResponseRedirect('/task_list')
    else:
        chn_task = CreateTask(initial={'name':task_obj.name, 'about':task_obj.about, 'image':task_obj.image, 'expiration_date':task_obj.expiration_date, 'status':task_obj.status})
    return render(request, 'index.html', {'add_task': chn_task})

#создание записи
def create_task(request):
    if request.POST:
        add_task = CreateTask(request.POST, request.FILES)
        if add_task.is_valid():
            task_obj = Task()
            task_obj.name = add_task.cleaned_data['name']
            task_obj.about = add_task.cleaned_data['about']
            task_obj.image = add_task.cleaned_data['image']
            task_obj.expiration_date = add_task.cleaned_data['expiration_date']
            task_obj.status = add_task.cleaned_data['status']
            task_obj.save()
            return HttpResponseRedirect('/')
    else:
        add_task = CreateTask()
    return render(request, 'index.html', {'add_task': add_task})

#статистика
def task_stat(request):
    tasks = dict(
        all_tasks = Task.objects.all().count(),
        open_tasks = Task.objects.filter(status='Open').count(),
        needs_offer_tasks = Task.objects.filter(status='Needs offer').count(),
        offered_tasks = Task.objects.filter(status='Offered').count(),
        approved_tasks = Task.objects.filter(status='Approved').count(),
        in_progress_tasks = Task.objects.filter(status='In progress').count(),
        ready_tasks = Task.objects.filter(status='Ready').count(),
        verified_tasks = Task.objects.filter(status='Verified').count(),
        closed_tasks = Task.objects.filter(status='Closed').count(),
        after_expiration_date = Task.objects.filter(expiration_date__lte=date.today()).count(),
    )
    return render(request, 'task_stat.html', {'tasks': tasks})


