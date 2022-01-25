from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/create/', views.createTask),
    path('tasks/<str:pk>/', views.getTask),
    path('tasks/<str:pk>/update', views.updateTask),
    path('tasks/<str:pk>/delete', views.deleteTask),
#     path('profiles/', views.getProfiles),
#     path('profiles/<str:pk>/', views.createProfile),
#     path('profiles/<str:pk>/', views.getProfile),
#     path('profiles/<str:pk>/update', views.updateProfile),
#     path('profiles/<str:pk>/delete', views.deleteProfile),
#     path('journals/', views.getJournals),
#     path('journals/<str:pk>/', views.createProfile),
#     path('journals/<str:pk>/', views.getProfile),
#     path('journals/<str:pk>/update', views.updateProfile),
#     path('journals/<str:pk>/delete', views.deleteJournal),
#     path('goals/', views.getGoals),
#     path('goals/<str:pk>/', views.createGoal),
#     path('goals/<str:pk>/', views.getGoal),
#     path('goals/<str:pk>/update', views.updateGoal),
#     path('goals/<str:pk>/delete', views.deleteGoal),
]
