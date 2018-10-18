from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .email import *


def homepage(request):
	if request.user.is_authenticated:
		if Join.objects.filter(user_id = request.user).exists():
			hood = Neighborhood.objects.get(pk = request.user.join.hood_id.id)
			posts = 'Posts.objects.filter(hood = request.user.join.hood_id.id)'
			businesses = "Business.objects.filter(hood = request.user.join.hood_id.id)"
			return render(request,'current_hood.html',{"hood":hood,"businesses":businesses,"posts":posts})
		else:
			hoods = Neighborhood.all_neighborhoods()
			return render(request,'index.html',{"hoods":hoods})
	else:
		hoods = Neighborhood.all_neighborhoods()
		return render(request,'index.html',{"hoods":hoods})



# def homepage(request):
#     hoods = Neighborhood.all_neighborhoods()

#     return render(request, 'index.html', {"hoods":hoods})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddHoodForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = current_user
            post.save()
        return redirect('homepage')

    else:
        form = AddHoodForm()
    return render(request, 'add_hood.html', {"form": form})


@login_required(login_url='/accounts/login/')
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddHoodForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = current_user
            post.save()
        return redirect('homepage')

    else:
        form = AddHoodForm()
    return render(request, 'add_hood.html', {"form": form})

@login_required(login_url='/accounts/login/')
def join_hood(request,hood_id):
	'''
	This view function will implement adding 
	'''
	neighborhood = Neighborhood.objects.get(pk = hood_id)
	if Join.objects.filter(user_id = request.user).exists():
		
		Join.objects.filter(user_id = request.user).update(hood_id = neighborhood)
	else:
		
		Join(user_id=request.user,hood_id = neighborhood).save()

	return redirect('add_profile')

@login_required(login_url='/accounts/login/')
def leave_hood(request,hood_id):
	'''
	This function will delete a neighbourhood instance in the join table
	'''
	if Join.objects.filter(user_id = request.user).exists():
		Join.objects.get(user_id = request.user).delete()
		messages.error(request, 'You have left this awesome neighborhood ;-(')
		return redirect('homepage')


@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    # posts = Post.get_profile_image(profile.id)
    title = f'@{profile.username}'
    return render(request, 'profile.html', {'title':title, 'profile':profile, 'profile_info':profile_info})
