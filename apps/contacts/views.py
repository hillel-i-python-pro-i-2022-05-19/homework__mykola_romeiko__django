from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def show_all(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request=request,
        template_name='contacts/show_all.html',
        context={'contacts': contacts}
    )


def create(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Contact was created.')
            return redirect('contacts:show_all')
    else:
        form = ContactForm()
    return render(
        request=request,
        template_name='contacts/create.html',
        context={'form': form}
    )


def view(request: HttpRequest, pk) -> HttpResponse:
    contact = get_object_or_404(klass=Contact, pk=pk)
    return render(
        request=request,
        template_name='contacts/view.html',
        context={'contact': contact}
    )


def edit(request: HttpRequest, pk) -> HttpResponse:
    contact = get_object_or_404(klass=Contact, pk=pk)
    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.info(request, 'Contact was edited.')
            return redirect('contacts:show_all')
    else:
        form = ContactForm(instance=contact)
    return render(
        request=request,
        template_name='contacts/edit.html',
        context={'form': form}
    )


def delete(request: HttpRequest, pk) -> HttpResponse:
    total_deleted, _ = Contact.objects.filter(pk=pk).delete()
    if total_deleted:
        messages.warning(request, 'Contact was deleted.')
    else:
        messages.info(request, 'Nothing was deleted.')
    return redirect('contacts:show_all')
