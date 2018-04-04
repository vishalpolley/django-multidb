from django.contrib import admin

from .models import form2

class form2Admin(admin.ModelAdmin):
	list_display = ["father_name", "mother_name"]
	class Meta:
		model = form2

admin.site.register(form2, form2Admin)
