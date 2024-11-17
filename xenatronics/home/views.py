from datetime import datetime

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm


def home(request):
    return render(request, 'home/home.html')

def custom_login_page(request):  # Renommée pour éviter le conflit
    return render(request, 'home/login.html')

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')



@login_required
def profile_view(request):
    profile = request.user.profile  # Accéder au profil lié
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        date_str = request.POST.get('birthday')
        if date_str:
            #date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            #profile.birthday = int(date_obj.timestamp() * 1000)
            #form['birthday'].value = str(date_obj)
            print(form['birthday'].value())

        if form.is_valid():
            form.save()
            messages.success(request, "Vos informations ont été mises à jour avec succès.")
            return redirect('home:profile')
        else:
            print(form.errors)
            messages.error(request, "Une erreur est survenue. Veuillez vérifier les champs.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'home/profile.html', {
            'user': request.user,
            'profile': form
        })


class CustomLoginView(LoginView):
    template_name = 'home/login.html'  # Chemin relatif au répertoire templates
    #redirect_authenticated_user = True

    def get_success_url(self):
        return '/profile/'  # Redirige vers la page de profil après connexion



class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
