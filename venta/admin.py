from django.contrib import admin
from .models import Category,PostProduct

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','published')
    readonly_fields=('created','updated')
    ordering=('author','published')
    search_fields=('title','author__username')
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(PostProduct,PostAdmin)



