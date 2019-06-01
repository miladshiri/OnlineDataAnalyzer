from django.contrib import admin
from .models import Data, Machine, Train, Predict

# Register your models here.

admin.site.register(Data)
admin.site.register(Machine)
admin.site.register(Train)
admin.site.register(Predict)
