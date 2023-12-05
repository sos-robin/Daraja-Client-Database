from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def home(request):
   clients = Client.objects.all()
   payments = Payment.objects.all()
   total_clients = clients.count()
   clients_completed_paments = payments.filter(status='Completed').count()
   total_revenue = sum(payment.product.price for payment in payments.filter(status='Completed'))
   pending_payments = payments.filter(status__in=['Unpaid', 'Incomplete']).count()

   context ={'clients':clients,'payments':payments,'total_clients':total_clients,
              'clients_completed_paments':clients_completed_paments,'total_revenue':total_revenue,'pending_payments':pending_payments}

   return render(request,'client/index.html',context)

def Client_List(request):
   clients = Client.objects.all()
   payments = Payment.objects.all()
   

   context ={'clients':clients,
             'payments':payments}
   return render (request,'client/client_list.html' ,context)
def Client_Payments(request):
   clients = Client.objects.all()
   payments = Payment.objects.all()
   
   context ={'clients':clients,'payments':payments,}

   return render(request,'client/client_payments.html',context)

def Clients_data(request,cd_ID):
   client =Client.objects.get(id=cd_ID)

   context={
      'client':client,
   }
   return render(request,'client/client_data.html',context)
def Clients_pay (request, cp_id):
   client = Client.objects.get(id=cp_id)
   context = {
      'client':client,
   }
   return render(request,'client/billing.html',context)
def Client_Info(request):
   return render (request, 'client/client_data.html')

def Billing(request): 
   return render (request,'client/billing.html')

def General_Notes(request):
   return render (request,'client/general-notes.html')

def Client_Documents(request):
   return render(request,'client/client_docs.html')

def createClient(request):
   form = ClientForm()
   if request.method == "POST":
      #print('Printing POST:',request.POST)
      form = ClientForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, 'Client created Successfully.')
         return redirect('Clients')
   context = {'form':form}
   return render(request, 'client/client_form.html',context)
def updateClient(request, pku):
   client = Client.objects.get(id=pku)
   form = ClientForm(instance=client)
   if request.method == "POST":
      form = ClientForm(request.POST, instance=client)
      if form.is_valid():
         form.save()
         return redirect('Clients')
   context = {'form':form}
   return render(request, 'client/client_form.html',context)

def deleteClient(request, pku):
   client = Client.objects.get(id=pku)
   if request.method == "POST":
      client.delete()
      messages.success(request, 'Client Removed Successfully.')
      return redirect('Clients')
   context ={'client':client}
   return render(request, 'client/delete.html',context)

def editPersonalinfo(request, pku):
   client = Client.objects.get(id=pku)
   form = personalInfoForm(instance=client)
   if request.method == "POST":
       form = personalInfoForm(request.POST, instance=client)
       if form.is_valid():
         form.save()
         cd_ID = client.id
         url = reverse('clients_data', kwargs={'cd_ID': cd_ID})
         return redirect(url)
         #return redirect('clients_data')
   context = {'form':form}
   return render(request, 'client/personal_info.html',context)

def editcompanyinfo(request, pku):
   client = Client.objects.get(id=pku)
   form = companyInfoForm(instance=client)
   if request.method == "POST":
       form = companyInfoForm(request.POST, instance=client)
       if form.is_valid():
         form.save()
         cd_ID = client.id
         url = reverse('clients_data', kwargs={'cd_ID': cd_ID})
         return redirect(url)
         #return redirect('clients_data')
   context = {'form':form}
   return render(request, 'client/company_info.html',context)

def profilePic(request, pku):
   client = Client.objects.get(id=pku)
   form = profilepicForm()
   if request.method == "POST":
      #print('Printing POST:',request.POST)
      form = profilepicForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         cd_ID = client.id
         url = reverse('clients_data', kwargs={'cd_ID': cd_ID})
         return redirect(url)
   context = {'form':form}
   return render(request, 'client/client_data.html',context)     








