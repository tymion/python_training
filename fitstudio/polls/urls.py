from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^index.html', views.get_name, name='index'),
    re_path(r'^ajax/calendar/$', views.get_fullcalendar_data, name='get_fullcalendar_data'),
    path('', views.index, name='index'),
    path('schedule.html', views.schedule, name='schedule'),
    path('category.html', views.category, name='category'),
    path('time.html', views.time, name='time'),
]
