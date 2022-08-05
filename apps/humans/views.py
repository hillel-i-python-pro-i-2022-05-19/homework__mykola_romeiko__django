from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from .forms import HumanForm
from .models import Human


def show_all(request: HttpRequest) -> HttpResponse:
    humans = Human.objects.all()
    return render(
        request=request,
        template_name='humans/show_all.html',
        context={'humans': humans}
    )


def create(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Human was created.')
            return redirect('humans:show_all')
    else:
        form = HumanForm()
    return render(
        request=request,
        template_name='humans/create.html',
        context={'form': form}
    )


def edit(request: HttpRequest, pk) -> HttpResponse:
    human = get_object_or_404(klass=Human, pk=pk)
    if request.POST:
        form = HumanForm(request.POST, instance=human)
        if form.is_valid():
            form.save()
            messages.info(request, 'Human was edited.')
            return redirect('humans:show_all')
    else:
        form = HumanForm()
    return render(
        request=request,
        template_name='humans/edit.html',
        context={'form': form}
    )


def delete(request: HttpRequest, pk) -> HttpResponse:
    total_deleted, _ = Human.objects.filter(pk=pk).delete()
    if total_deleted:
        messages.warning(request, 'Human was deleted.')
    else:
        messages.info(request, 'Nothing was deleted.')
    return redirect('humans:show_all')
