from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:request_id>/', views.detail, name='detail'),
    path('<int:request_id>/results/', views.results, name='results'),
    path('<int:request_id>/vote/', views.vote, name='vote'),
]

