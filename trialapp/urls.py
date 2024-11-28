from django.urls import path
from .import views


urlpatterns = [
    path('',views.mainproject,name="mainproject"),
    path('project_two/<str:pk>/',views.project_two,name="project_two"),
    path('project/<str:pk>/',views.project,name="project"),
    path('create-project/',views.Createproject,name="create-project"),
    path('Updateproject/<str:pk>/',views.Updateproject,name="Updateproject"),
    path('deleteproject/<str:pk>/',views.deleteproject,name="deleteproject"),
]
