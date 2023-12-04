from django.shortcuts import render, redirect
from .models import contact
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.


def landing(request):
    return render(request, 'index.html')


def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Message sent successfully")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})