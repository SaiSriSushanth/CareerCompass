from django.urls import path
from . import views

app_name = "roadmaps"

urlpatterns = [
    path('', views.roadmaps_list, name="list"),
    path('new-roadmap/', views.roadmap_new, name="new-roadmap"),
    path('<slug:slug>', views.roadmap_page, name="page"),
]