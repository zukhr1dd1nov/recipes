from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView , FormView , UpdateView
from .forms import RegistrationForm, LoginForm, ProfileForm, ChangePasswordForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin ,UpdateView):
    template_name = "account/profile.html"
    form_class = ProfileForm
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, _("Muvaffaqiyalti o'zgartirildi"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account_profile')

class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(self.request , **form.cleaned_data)
        if user is not None:
            login(self.request , user)
            messages.success(self.request , _(f"Xush kelibsiz {user.get_full_name()}"))
            return  redirect('main_index')

        form.add_error('password',_("Login va/yoki parol notog'ri"))
        return self.form_invalid(form)

class RegistrationView(CreateView):
    template_name = "account/registration.html"
    model = User
    form_class = RegistrationForm

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data.get('password'))
        messages.success(self.request,_("Muvaffaqiyatli ro'yhatdan o'tdingiz"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account_login')

@login_required
def account_logout(request):
    messages.success(request,_(f"Kelib turing , {request.user.get_full_name()}"))
    logout(request)
    return redirect("main_index")

class ChangePasswordView(LoginRequiredMixin ,FormView):
    template_name = "account/change-password.html"
    form_class = ChangePasswordForm

    def form_valid(self, form):
        self.request.user.set_password(form.cleaned_data.get('new_password'))
        self.request.user.save()
        messages.success(self.request,_("Parol muvaffaqiyatli o'zgartirildi"))
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('change_password')