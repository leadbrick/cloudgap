from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth
#from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.http import Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from forms import LoginForm,NewUserForm
# Create your views here.

@csrf_protect
def register_user(request):
	if not request.POST:
		form=NewUserForm()
		return render_to_response("form_generic.html",{'form':form},RequestContext(request))
	elif request.POST:
		form=NewUserForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],password=form.cleaned_data['password1'])
			return HttpResponseRedirect('/')


def auth_login(request):
	if not request.POST:
		form=LoginForm()
		return render_to_response("form_generic.html",{'form':form},RequestContext(request))
	elif request.POST:
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password= form.cleaned_data['password']
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/account')
			else:
				errors = "Wrong Username Password Combination"
				return render_to_response("form_generic.html",{'errors':errors})

def user_logout(request):
	auth.logout(request)
	return render_to_response("loggedout.html")


def user_settings(request):
	if not request.POST:
		return render_to_response("account.html",RequestContext(request))
	else:
		return HttpResponseRedirect("/")

	