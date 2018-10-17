from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .email import *

def homepage(request):
    posts = "testing to link templates"

    return render(request, 'index.html', {"posts":posts})
