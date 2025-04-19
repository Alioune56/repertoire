from django.shortcuts import render,get_object_or_404
from .models import Contact
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'contact/index.html')
@login_required(login_url='/login/')
def contact_list(request):
    contact = Contact.objects.all()
    context = {'contacts':contact}
    return render(request,'contact/liste.html',context)
@login_required(login_url='/login/')
def contact_details(request,id):
    contact = get_object_or_404(Contact,id=id)
    context = {'contacts':contact}
    return render(request,'contact/contact_detail.html',context)