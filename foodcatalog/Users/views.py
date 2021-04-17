from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to the community {username}, your account has been created')
            return redirect('food')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })

@login_required
def profilepage(request):
    return render(request, 'profile.html', )
    """if user.is_authenticated:
        return render(request, 'profile.html', )
    
    else:
        return redirect('login')"""