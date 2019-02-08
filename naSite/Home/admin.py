from django.contrib import admin
from .models import NewsFeed, comment_page, news_application
from tinymce.widgets import TinyMCE
from django.db import models

class NewsFeedAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class CommentPageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(comment_page, CommentPageAdmin)
admin.site.register(NewsFeed, NewsFeedAdmin)
admin.site.register(news_application)