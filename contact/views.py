from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/contact_detail.html', {'contact': contact})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Envoyer un e-mail (exemple)
            send_mail(
                'Nouveau message de contact',
                f'Vous avez reçu un nouveau message de {contact.full_name}. Sujet: {contact.subject}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
            return redirect('contact:contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:contact_list')
    return render(request, 'contact/contact_confirm_delete.html', {'contact': contact})
