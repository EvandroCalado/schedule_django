from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User created.')
            return redirect('contact:index')

    context = {
        'form': RegisterForm(),
    }

    return render(request, 'contact/register.html', context)
