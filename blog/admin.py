from django.contrib import admin
from .models import Contact, Post

# PostAdmin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

# ContactAdmin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'message']