from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView, DeleteView

