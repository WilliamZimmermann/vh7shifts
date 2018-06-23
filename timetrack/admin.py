from django.contrib import admin

# Register your models here.
from timetrack.models import Company, Location, AutoBreakRules

admin.site.register(Company)
admin.site.register(Location)
admin.site.register(AutoBreakRules)
