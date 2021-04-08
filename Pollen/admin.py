from django.contrib import admin
from .models import Image, Text
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'photo']

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	list_display = ['id', 'city']