from django.contrib import admin
from kitten.models import User, Job, Status

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Status)