from django.shortcuts import render, get_object_or_404
from .models import ManagerModel
from .forms import ManagerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/admin/')
def manager_list(request):
    contacts = ManagerModel.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'manager/contact-list', {'contacts': contacts})


@login_required(login_url='/admin/')
def create(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return render(request, 'manager/partials/contact-item.html', {'contact': contact})
    return render(request, 'manager/contact-list.html', {'form': ManagerForm()})


@login_required(login_url='/admin/')
def update(request, id):
    contact = get_object_or_404(ManagerModel, id=id, user=request.user)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=contact)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.user = request.user
            new_contact.save()
            return render(request, 'manager/partials/contact-item.html', {'contact': new_contact})
    return render(request, 'manager/contact-list', {'contact': contact, 'form': ManagerForm(instance=contact)})


@login_required(login_url='/admin/')
def delete(request, id):
    contact = get_object_or_404(ManagerModel, id=id, user=request.user)
    contact.delete()
    return ""