from django.urls import path
from . import views

app_name = 'machine'

urlpatterns = [
    path('upload_data/', views.upload_data, name='upload_data'),
  #  path('model_data/', views, name='model_data'),
  #  path('predict/', views, name='predict'),

]