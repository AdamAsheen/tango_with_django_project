from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Customizing the admin interface

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

# Register your models here
admin.site.register(Page, PageAdmin)  # Register the Page model with PageAdmin

admin.site.register(UserProfile)
