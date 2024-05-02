from .models import Usuari, Rol
from django.forms import ModelForm


class UsuariForm(ModelForm):
    class Meta:
        model = Usuari
        fields = "__all__"
