from django.http import Http404
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm()
    return render(request, 'pages/register_view.html', {'form': form})


def register_create(request):
    if request.method != 'POST':
        raise Http404()

    form = RegisterForm(request.POST)

    if not form.is_valid():
        return render(request, 'pages/register_view.html', {
            'form': form
        })

    return redirect('authors:register')
