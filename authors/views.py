from django.http import Http404
from django.shortcuts import redirect, render
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm()
    return render(request,'pages/register_view.html',{
        'form':form
    })

def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    return redirect('authors:register')