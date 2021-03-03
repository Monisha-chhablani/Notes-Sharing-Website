from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Signup)
admin.site.register(Notes)

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
