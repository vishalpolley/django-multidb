from django import forms

from .models import form1

class TestForm1(forms.ModelForm):
	class Meta:
		model = form1
		fields = ['first_name', 'last_name']
		widgets = {
					'first_name': forms.TextInput(attrs={
						'id': 'first_name',
						}),
					'last_name': forms.TextInput(attrs={
						'id': 'last_name',
						}),
		}

	def __init__(self, *args, **kwargs):
		super(TestForm1, self).__init__(*args, **kwargs)
		self.fields['first_name'].label = ''
		self.fields['last_name'].label = ''