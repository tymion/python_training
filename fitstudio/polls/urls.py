from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path('^index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('schedule.html', views.schedule, name='schedule'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
