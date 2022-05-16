from django.contrib import admin

from .models import creator, dashCode, dashboard

admin.site.register(dashboard)
admin.site.register(dashCode)
admin.site.register(creator)