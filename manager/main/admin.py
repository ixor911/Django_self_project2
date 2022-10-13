from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Chat)
admin.site.register(Task)
admin.site.register(Message)

