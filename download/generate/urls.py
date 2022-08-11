from django.urls import path

from .import views

urlpatterns = [
    path('new', views.new, name='new'),
    path('template', views.template, name='template'),
    # url path for download
    path('dpdf/', views.downloadpdf.as_view(), name='pdf'),
]