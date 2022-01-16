from datetime import datetime
from email.policy import default
from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    clave = forms.CharField()
    tipo = forms.CharField()
    
class PublicacionesForm(forms.Form):
    titulo = forms.CharField()
    nombre = forms.CharField()
    noticia = forms.CharField(widget=forms.Textarea())
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True)