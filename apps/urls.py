from django.urls import path 

from .views import ListForm, titleView

urlpatterns = [
    path('', ListForm.as_view(), name='index'),
    path('form/<str:slug>', titleView, name='form')
    # path('create/form/', FormView.as_view(), name='create-form')
]