from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import InscriptionForm
from .forms import PortefeuilleForm
from .models import DocumentFinancier
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'portfolio/Home.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrement de l'utilisateur
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authentification automatique après l'inscription
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Connexion automatique de l'utilisateur
                return redirect('home')  # Redirection vers la page d'accueil ou autre vue
    else:
        form = InscriptionForm()
    return render(request, 'portfolio/inscription.html', {'form': form})  # Utilisation du bon template

def creer_portefeuille(request):
    if request.method == 'POST':
        form = PortefeuilleForm(request.POST)
        if form.is_valid():
            portefeuille = form.save(commit=False)
            portefeuille.utilisateur = request.user
            portefeuille.save()
            return redirect('liste_portefeuilles')
    else:
        form = PortefeuilleForm()
    return render(request, 'portfolio/creer_portefeuille.html', {'form': form})

def upload_document(request):
    if request.method == 'POST':
        fichier = request.FILES['fichier']
        entreprise_id = request.POST['entreprise']
        document = DocumentFinancier(fichier=fichier, entreprise_id=entreprise_id)
        document.save()
        return redirect('liste_documents')
    return render(request, 'portfolio/upload_document.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Authentifie l'utilisateur
        if user is not None:
            login(request, user)  # Connecte l'utilisateur
            return redirect('home')  # Redirige vers la page d'accueil après connexion
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")  # Affiche un message d'erreur
    return render(request, 'Portfolio/login.html')  # Affiche la page de connexion