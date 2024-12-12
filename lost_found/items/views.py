from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .models import FoundItem
from .forms import FoundForm
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            items = FoundItem.objects.all()
            return render(request, 'found_list.html', {'items': items})
  # Updated to match the name in urls.py
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
@login_required
def FoundItem_list(request):
    items = FoundItem.objects.all()
    return render(request, 'found_list.html', {'items': items})
@login_required
def FoundItem_create(request):
    if request.method == "POST":
        form = FoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('found_list')  # Updated to match the name in urls.py
    else:
        form = FoundForm()
    return render(request, 'found_form.html', {'form': form})