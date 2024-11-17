from django.urls import path

from .views import home, about, index, custom_login_page, CustomLoginView, CustomLogoutView, profile_view

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('index/', index, name='index'),
    path('profile/', profile_view, name='profile'),  # Page de profil
    path('login/', CustomLoginView.as_view(), name='login'),  # Login via LoginView
    path('logout/', CustomLogoutView.as_view(next_page='/login/'), name='logout'),  # Logout via LogoutView
    path('custom-login-page/', custom_login_page, name='custom_login_page'),  # Page personnalisée
]
