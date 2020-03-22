from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('list/', views.ListUsers.as_view(), name='list'),
    path('create/', views.CreateUser.as_view(), name='create'),
    path('<int:pk>/read/', views.ReadUser.as_view(), name='read'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete'),
]
