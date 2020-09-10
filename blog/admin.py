from django.contrib import admin
from blog.models import  Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','pub_date']
    fields = ['title','author','pub_date', 'post']
admin.site.register(Post,PostAdmin)

