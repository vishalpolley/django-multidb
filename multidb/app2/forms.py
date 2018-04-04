from django import forms

from .models import form2

class TestForm2(forms.ModelForm):
	class Meta:
		model = form2
		fields = ['father_name', 'mother_name']
		widgets = {
					'father_name': forms.TextInput(attrs={
						'id': 'father_name',
						}),
					'mother_name': forms.TextInput(attrs={
						'id': 'mother_name',
						}),
		}

	def __init__(self, *args, **kwargs):
		super(TestForm2, self).__init__(*args, **kwargs)
		self.fields['father_name'].label = ''
		self.fields['mother_name'].label = ''