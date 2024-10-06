from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portefeuille
from .models import Investissement
from django import forms

class InscriptionForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PortefeuilleForm(forms.ModelForm):
    class Meta:
        model = Portefeuille
        fields = ['nom']

class InvestissementForm(forms.ModelForm):
    class Meta:
        model = Investissement
        fields = ['type_investissement', 'nombre_actions', 'valeur_actuelle', 'entreprise']

