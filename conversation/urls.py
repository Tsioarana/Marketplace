from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
  path('inbox/', views.inbox, name='inbox'),
  path('detail/<int:pk>/', views.detail, name='detail'),
  path('new/<int:item_pk>/', views.new_conversation, name='new')
]
