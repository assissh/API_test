from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializers
from .serializers import *
from .models import *

from .forms import User_form



def User(request):
    form = User_form(request.POST)
    context = {"form":form}
    if form.is_valid():
        form.save()

    return render(request,"user.html",context)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User_Profile.objects.all()
    serializer_class = UserSerializers





