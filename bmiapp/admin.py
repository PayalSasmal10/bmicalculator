import imp
from django.contrib import admin
from .models import BMI
# Register your models here.

class BMIAdmin(admin.ModelAdmin):
    list_display = ('user', 'bmi', 'date')


admin.site.register(BMI, BMIAdmin)

