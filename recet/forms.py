from django import forms
from .models import Receta

class RecetForm(forms.ModelForm): #cada formulario es una clase
	class Meta:
		model = Receta
		fields = '__all__'