from django.contrib import admin
from .models import JobModel, JobImage

class JobImageInline(admin.TabularInline):
    model = JobImage

# class AdditionalJobImageInline(admin.TabularInline):
#     model = AdditionalJobImage

@admin.register(JobModel)
class JobModelAdmin(admin.ModelAdmin):
    inlines = [JobImageInline]

@admin.register(JobImage)
class JobImageAdmin(admin.ModelAdmin):
    pass

# @admin.register(AdditionalJobImage)
# class AdditionalJobImageAdmin(admin.ModelAdmin):
#     pass