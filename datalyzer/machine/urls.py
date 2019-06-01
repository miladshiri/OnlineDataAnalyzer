from django.urls import path
from . import views

app_name = 'machine'

urlpatterns = [
    path('select_method/', views.select_method, name='select_method'),
    path('config_machine/', views.config_machine, name='config_machine'),
    path('model_data/', views.model_data, name='model_data'),
    path('predict_data/', views.predict_data, name='predict_data'),

    path('dataset/upload/', views.upload_data, name='upload_data'),
    path('dataset/<int:pk>/delete/', views.DataDelete.as_view(), name='delete_data'),
    path('dataset/<int:pk>/detail/', views.DataDetail.as_view(), name='detail_data'),
    path('datasets/', views.DataList.as_view(), name='data_list'),

    #  path('predict/', views, name='predict'),

]