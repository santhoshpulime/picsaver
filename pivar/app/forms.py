from django import forms

from .models import pics,text



class picform(forms.ModelForm):
	class Meta:
		model = pics
		fields = "__all__"