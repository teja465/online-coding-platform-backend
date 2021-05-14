from django.contrib import admin
from . import models
# Register your models here.
my_models =[models.problem,models.test_case]

admin.site.register(my_models)