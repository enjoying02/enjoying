from django.contrib import admin
from .models import Subject, Category

admin.site.register(Subject)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)