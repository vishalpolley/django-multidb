from django.db import models

class form2(models.Model):
	father_name = models.CharField(max_length=50, blank=False, null=False)
	mother_name = models.CharField(max_length=50, blank=False, null=False)

	class Meta:
		app_label = 'app2'
		verbose_name = 'Form2'
		verbose_name_plural = 'Forms2'

	def __str__(self):
		return self.father_name
