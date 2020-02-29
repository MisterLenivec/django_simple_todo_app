from django.urls import path
from .views import index, update_task, delete_task


urlpatterns = [
    path('', index, name='list'),
    path('update_task/<str:pk>/', update_task, name='update_task'),
    path('delete_task/<str:pk>/', delete_task, name='delete_task'),
]
