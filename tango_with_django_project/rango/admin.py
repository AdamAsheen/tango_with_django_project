from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Customizing the admin interface

# Register your models here
admin.site.register(Category)  # Register the Category model
admin.site.register(Page, PageAdmin)  # Register the Page model with PageAdmin
