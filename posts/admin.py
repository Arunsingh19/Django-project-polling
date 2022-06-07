from django.contrib import admin

from posts.models import Post, vote

admin.site.register(Post)
admin.site.register(vote)
