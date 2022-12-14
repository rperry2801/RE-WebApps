from django.db import models

# Create your models here.
class Lead(models.Model):
	# lead_rep = models.CharField(max_length=200)

	lead_name = models.CharField(max_length=200)
	lead_addr = models.CharField(max_length=200)
	lead_descript = models.TextField()
	lead_received = models.DateTimeField('Date Received')

	# TODO - CREATE DROP-DOWN AS PART OF MODEL FOR "LEAD STATUS"

	class Meta:
		verbose_name_plural = "Leads"

	def __str__(self):
		return self.lead_name

class CreateLead(models.Model):

	contact = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	notes = models.TextField()
	received = models.DateTimeField('Date Received')

	class Meta:
		verbose_name_plural = "Created Leads"

	def __str__(self):
		return self.contact