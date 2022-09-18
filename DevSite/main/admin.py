from django.contrib import admin
from .models import Lead

# Register your models here.
class LeadAdmin(admin.ModelAdmin):
	fields = ["lead_name",
			  "lead_addr",
			  "lead_descript",
			  "lead_received"]

admin.site.register(Lead,LeadAdmin)