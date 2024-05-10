from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SignupForm, ChangePasswordForm, UpdateProfileForm
# views.py

from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm

# class CustomPasswordResetView(PasswordResetView):
#     form_class = CustomPasswordResetForm
#     template_name = 'myapp/password_reset_form.html'
#     email_template_name = 'myapp/password_reset_email.html'
#     success_url = '/' 

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Ajoutez les valeurs uidb64 et token au contexte
#         context['uidb64'] = self.kwargs.get('uidb64')
#         context['token'] = self.kwargs.get('token')
#         return context

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, 'myapp/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'myapp/contact.html')

# Auth
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'myapp/signup.html', {
        'form': form
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'myapp/change_password.html', {
        'form': form
    })

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'myapp/update_profile.html', {
        'form': form
    })

@login_required
def profile(request):
    return render(request, 'myapp/profile.html')
