"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from account.views import RegistrationView, LoginView, account_logout, ProfileView, ChangePasswordView
from main.views import main_index, main_kategoriya, main_taom, TaomView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('i18/',include('django.conf.urls.i18n'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
                  path('', main_index, name='main_index'),
                  path('kategoriya/<int:rid>/', main_kategoriya, name='main_retsept'),
                  path('taom/<int:pid>/', main_taom, name='main_read'),
                  path('account/registration/', RegistrationView.as_view() , name="account_registration"),
                  path('taom/add/', TaomView.as_view() , name="main_taom"),
                  path('account/change-password/', ChangePasswordView.as_view() , name="change_password"),
                  path('account/login/', LoginView.as_view(), name='account_login'),
                  path('account/logout/', account_logout, name='account_logout'),
                  path('account/profile/', ProfileView.as_view(), name='account_profile'),
)
