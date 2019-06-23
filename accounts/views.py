from django import forms
from django.shortcuts import render
from django.views.generic import UpdateView
from accounts.models import User, Profile
from accounts.forms import UserForm, EditUserForm, EditProfileForm
# from django.core.validators import MaxValueValidator, MinValueValidator 
# Authentication imports:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from User form and Profile form:
        user_form = UserForm(data=request.POST)

        # Check to see if both forms are valid:
        if user_form.is_valid(): # and profile_form.is_valid():

            # Save user form to database and hash password:
            user = user_form.save()
            # user.set_password(user.password) ###########################
            user.save()

            # Update registration status
            registered = True

            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password1'])

            login(request, user)
            return HttpResponseRedirect(reverse('accounts:edit_profile'))

        else: # if one of the forms is invalid:
            print(user_form.errors) # MANIUPLATE THIS!

    else: # if no post request, then render the forms as blank
        user_form = UserForm()

    template_name = 'register.html'
    context = {
    'user_form':user_form,
     # 'profile_form':profile_form,
     'registered':registered
    }
    return render(request, template_name, context)

def user_login(request):

    if request.method == 'POST':
        # First, get the username and Password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # User Django's authentication function:
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # if the user is active, log them in:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            context = {
                'invalid':True,
            }
    else:
        context = {}

    template_name = 'login.html'
    return render(request, template_name, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:user_login'))

@login_required
def edit_profile(request):

    updated = False
    invalid = False

    if request.method == 'POST':
        user_form = EditUserForm(data=request.POST, instance=request.user)
        profile_form = EditProfileForm(data=request.POST, instance=request.user.profile)

        # helper function to verify if all of the forms are valid.
        def forms_are_valid():
            user = user_form.is_valid()
            profile = profile_form.is_valid()

            return user and profile

        if forms_are_valid():

            user = user_form.save()
            profile = profile_form.save(commit=False)


            # Save model:
            user.save()
            profile.save()

            updated = True
            invalid = False

        else:
            invalid = True

    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

    template_name = 'user.html'

    context = {
        'user_form':user_form,
        'updated':updated,
        'invalid':invalid,
        'user':request.user,
        'profile_form':profile_form,
    }
    
    return render(request, template_name, context)