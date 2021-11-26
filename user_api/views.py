from django.shortcuts import render
from isort import Config

from .forms import UserForm
from django.http import HttpResponseRedirect

# Create your views here.

def User_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render (request,{'form':form})

    form = UserForm()
    return render(request,{'form':form})


def check_size(image):
    image.seek(0,2)
    size = image.tell()
    if int(size) > int(Config.Image_Size):
        return False
    return True

