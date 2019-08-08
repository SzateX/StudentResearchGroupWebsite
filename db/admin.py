from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Profile, RepoLink, Article, Tag, File, Section, Gallery])
