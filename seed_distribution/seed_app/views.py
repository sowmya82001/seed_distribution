from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Seed, Distribution, Farmer
from .models import Contact  # Import Contact model if storing messages
from .forms import ContactForm  # Import form if using Django Forms
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

@login_required
def dashboard(request):
    seeds = Seed.objects.all()
    farmers = Farmer.objects.all()
    distributions = Distribution.objects.all()
    return render(request, 'dashboard.html', {'seeds': seeds, 'farmers': farmers, 'distributions': distributions})

def dashboard(request):
    seeds = Seed.objects.all()
    farmers = Farmer.objects.all()
    distributions = Distribution.objects.all()
    return render(request, 'dashboard.html', {'seeds': seeds, 'farmers': farmers, 'distributions': distributions})

def seeds_view(request):
    seeds = Seed.objects.all()
    return render(request, 'seeds.html', {'seeds': seeds})

def farmers_view(request):
    farmers = Farmer.objects.all()
    return render(request, 'farmers.html', {'farmers': farmers})

def distributions_view(request):
    distributions = Distribution.objects.all()
    return render(request, 'distributions.html', {'distributions': distributions})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB if using Django model
            send_mail(
                subject=f"Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@example.com'],  # Change to your email
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
