from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date_posted','tags')
    search_fields = ('title',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display =('post','text','created_date','author','approved_comment')

admin.site.register(Comment,CommentAdmin)

