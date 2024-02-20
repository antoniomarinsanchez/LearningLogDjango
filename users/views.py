from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registers a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Stats the users session
            login(request, new_user)
            return redirect('learning_logs:index')

    # Shows the empty form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

