from django.contrib import admin
from .models import projects,review,tag

# Register your models here.
admin.site.register(projects)
admin.site.register(review)
admin.site.register(tag)
