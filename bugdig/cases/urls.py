from django.urls import path

from . import views

app_name = 'cases'

urlpatterns = [
    path('list/', views.ListCases.as_view(), name='list'),
    path('create/', views.CreateCase.as_view(), name='create'),
    path('<int:pk>/read/', views.ReadCase.as_view(), name='read'),
    path('<int:pk>/update/', views.UpdateCase.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteCase.as_view(), name='delete'),
]
