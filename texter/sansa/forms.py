from django import forms
from .models import InputText

class TextForm(forms.ModelForm):
	class Meta:
		model = InputText
		fields = ['body']
		widgets = {
			'body': forms.Textarea()
		}