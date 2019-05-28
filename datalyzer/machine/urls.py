from django.urls import path
from . import views

app_name = 'machine'

urlpatterns = [
    path('upload_data/', views.upload_data, name='upload_data'),
    path('select_method/', views.select_method, name='select_method'),
    path('config_machine/', views.config_machine, name='config_machine'),
    path('model_data/', views.model_data, name='model_data'),

    #  path('predict/', views, name='predict'),

]