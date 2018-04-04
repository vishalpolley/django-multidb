from django.db import models

class form1(models.Model):
	first_name = models.CharField(max_length=50, blank=False, null=False)
	last_name = models.CharField(max_length=50, blank=False, null=False)

	class Meta:
		app_label = 'app1'
		verbose_name = 'Form1'
		verbose_name_plural = 'Forms1'

	def __str__(self):
		return self.first_name
