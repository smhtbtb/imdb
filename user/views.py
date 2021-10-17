from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from user.forms import UserLoginForm, RegistrationForm, MyPasswordChangeForm


class MyView(generic.TemplateView):
    template_name = 'base.html'


# Login View
class MyLoginView(LoginView):
    template_name = "customer_temp/login.html"
    authentication_form = UserLoginForm


# Register View
def register(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(phone=phone, password=raw_password)
            login(request, account)

            return redirect('customer:baseview')
        else:
            context['registration_form'] = form
    elif request.method == 'GET':
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'customer_temp/register_form.html', context)


# # Change Password View
# class MyPasswordChangeView(PasswordChangeView):
#     form_class = MyPasswordChangeForm
#     template_name = "customer_temp/change_password.html"
#     success_url = reverse_lazy('customer:baseview')
