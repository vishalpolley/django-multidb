from django.contrib import admin

from .models import form1

class form1Admin(admin.ModelAdmin):
	list_display = ["first_name", "last_name"]
	class Meta:
		model = form1

admin.site.register(form1, form1Admin)
