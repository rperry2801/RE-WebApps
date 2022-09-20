from django.contrib import admin
from .models import Lead
from .models import CreateLead
from .forms import LeadCreationForm

# Register your models here.
class LeadAdmin(admin.ModelAdmin):
	fields = ["lead_name",
			  "lead_addr",
			  "lead_descript",
			  "lead_received"]

class CreateLeadAdmin(admin.ModelAdmin):

	form = LeadCreationForm

	fields = ["contact",
			  "address",
			  "notes",
			  "received"]

admin.site.register(CreateLead, CreateLeadAdmin)
admin.site.register(Lead,LeadAdmin)