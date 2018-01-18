from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path('^index.html', views.index, name='index'),
    re_path(r'^ajax/calendar/$', views.get_events, name='get_events'),
    path('', views.index, name='index'),
    path('schedule.html', views.schedule, name='schedule'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
]
