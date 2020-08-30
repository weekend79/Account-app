from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Retruns the registration view"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def profile(request):
    """Returns the user profile page"""
    user = User.objects.get(username=request.user.username)
    return render(request, 'registration/profile.html')


