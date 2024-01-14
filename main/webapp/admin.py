from django.contrib import admin
from . models import JobModel, JobImage

# Register your models here.
admin.site.register(JobModel)
admin.site.register(JobImage)