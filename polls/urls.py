from django.urls import path
from . import views

app_name = 'polls'
urlpatterns=[
	path('',views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]