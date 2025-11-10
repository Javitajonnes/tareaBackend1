from django.contrib import admin
from .models import LinkRed

class LinkRedAdmin(admin.ModelAdmin):
    pass
admin.site.register(LinkRed,LinkRedAdmin)