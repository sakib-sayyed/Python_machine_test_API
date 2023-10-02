from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('clients/',ClientsListView.as_view()),
    path('clients/<int:pk>/',ClientDetail.as_view()),
    path('clients/<int:pk>/projects/', ProjectForClient.as_view()),
    path('user-projects/', UserProjects.as_view()),
]
