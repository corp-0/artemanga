from django import forms
from .models import Mensaje
from ckeditor.widgets import CKEditorWidget

class CrearMensajeForm(forms.Form):
    texto = forms.CharField(label=False, widget=CKEditorWidget())

    class Meta:
        fields = ['texto']
        model = Mensaje