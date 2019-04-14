from django.conf.urls import url
from task_list import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.create_task, name='create_task'),
    url(r'^task_list/$', views.task_list, name='task_list'),
    url(r'^task/(\d+)$', views.task, name='task'),
    url(r'^change/(\d+)$', views.change_task, name='change_task'),
    url(r'^delete/(\d+)$', views.del_task, name='del_task'),
    url(r'^task_stat/$', views.task_stat, name='task_stat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

