from django.contrib import admin
from .models import Profile, tag, Location, Project, Comment, Ratings

# Register your models here.
admin.site.register(Profile)
admin.site.register(tag)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Ratings)
