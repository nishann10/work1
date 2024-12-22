from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.
def softadd(request):
    if request.method == 'POST':
        firstname1=request.POST.get('first_name')
        lastname1=request.POST.get('last_name')
        email1=request.POST.get('e_mail')
        department1=request.POST.get('de_partment')
        disignation1=request.POST.get('de_signation')
        dateofjoin1=request.POST.get('date_ofjoin')
        salery1=request.POST.get('sa_lery')
        photo1=request.FILES.get('ph_to')
        soft_obj=soft()
        soft_obj.firstname=firstname1
        soft_obj.lastname=lastname1
        soft_obj.email=email1
        soft_obj.department=department1
        soft_obj.disignation=disignation1
        soft_obj.dateofjoin=dateofjoin1
        soft_obj.salery=salery1
        soft_obj.photo=photo1
        soft_obj.save()
        return redirect('so1')
    return render(request,"soft_add.html")
def softget(request):
    ab=soft.objects.all()
    return render(request,"soft_get.html",{'a':ab})
def softupdate(request,id):
    ab=soft.objects.get(id=id)
    if request.method == 'POST':
        firstname1=request.POST.get('first_name')
        lastname1=request.POST.get('last_name')
        email1=request.POST.get('e_mail')
        department1=request.POST.get('de_partment')
        disignation1=request.POST.get('de_signation')
        dateofjoin1=request.POST.get('date_ofjoin')
        salery1=request.POST.get('sa_lery')
        photo1=request.FILES.get('ph_to')
        ab.firstname=firstname1
        ab.lastname=lastname1
        ab.email=email1
        ab.department=department1
        ab.disignation=disignation1
        ab.dateofjoin=dateofjoin1
        ab.salery=salery1
        ab.photo=photo1
        ab.save()
        return redirect('so1')
    return render(request,"soft_update.html",{'a':ab})
def softdelete(request,id):
    ab=soft.objects.get(id=id)    
    ab.delete()
    return redirect('so1')
