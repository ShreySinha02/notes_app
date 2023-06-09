from django.urls import path
from api import views

urlpatterns = [
    path('',views.getRoute),
    path('notes/',views.getNotes),
    path('notes/create/', views.createNote, name="create-note"),
    path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    path('notes/<str:pk>/', views.getNote, name="note"),

]
