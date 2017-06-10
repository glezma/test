# -*- coding: utf-8 -*-
""" manages views"""
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, LoginForm

# Create your views here.
def index(request):# index=name of the function to call
    """ deprecated """
    context = {'data_1' : 'Gonzalo'}
    return render(request, 'index/index.html', context)


class UserFormView(View):
    """ Initial form """
    form_class_signup = UserForm
    form_class_login = LoginForm
    template_name = 'index/index.html'

    # display blank` form
    def get(self, request):
        """ GET method manages landing get request"""
        form_signup = self.form_class_signup(None)
        form_login = self.form_class_login(None)
        return render(request, self.template_name,\
                    {'form_signup' : form_signup, 'form_login': form_login})

    def post(self, request):
        """ POST method manages both: signup and login"""

        if str(request.POST['send']) == 'sign_up_v':
            form_signup = self.form_class_signup(request.POST)
            form_login = self.form_class_login(None)
            if form_signup.is_valid():
                # Create, but don't save the new author instance.
                user = form_signup.save(commit=False)
                username = form_signup.cleaned_data['username']
                password = form_signup.cleaned_data['password']
                user.set_password(password)
                user.save()

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user) # request.user
                        return traininghub(request)
                else:
                    return HttpResponse('user is valid but none no authe')
            else:
                return render(request, self.template_name, {'form_signup' : form_signup, \
                                                    'form_login': form_login})
# LOGIN PROCESS
        else:
            form_login = self.form_class_login(request.POST)
            form_signup = self.form_class_signup(None)

            if form_login.is_valid():
                username = form_login.cleaned_data['username']
                password = form_login.cleaned_data['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)#
                        return redirect(reverse('index:p_home'))
                        # render(request,'index/training_hub.html',{'user' : user})
                else:
                    error = 'Invalid credentials'
                    return render(request, self.template_name, {'form_signup' : form_signup, \
                                                'form_login': form_login,\
                                                'error':error})


def logout_user(request):
    """ logout user """
    logout(request)
    return redirect(reverse("index:p_index"))

def cheatsheet(request):
    """ cheatsheet """
    if not request.user.is_authenticated():
        return redirect(reverse("index:p_index"))
    else:
        user = request.user
        context = {'user': user}
        return render(request, 'index/cheat_sheet.html', context)

def traininghub(request):
    """ training hub homepage"""
    if not request.user.is_authenticated():
        return redirect(reverse("index:p_index"))
    else:
        user = request.user
        context = {'user': user}
        return render(request, 'index/training_hub.html', context)
