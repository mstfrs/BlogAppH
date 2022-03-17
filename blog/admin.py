from django.contrib import admin
from .models import Likes, PostList, Comments

# Register your models here.

admin.site.register(PostList)
admin.site.register(Comments)
admin.site.register(Likes)
