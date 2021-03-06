# from trash_collector.customers.apps import CustomersConfig
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.apps import apps
from django.shortcuts import redirect, render
from .models import Customer
from django.urls import reverse


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user         
    try: 
        logged_in_customer = Customer.objects.get(user=user)
        context = { 
        'logged_in_customer': logged_in_customer
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
    }    
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('customers:create'))
    return render(request,'customers/index.html', context)

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
def create(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.user
        street_address = request.POST.get('street_address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup = request.POST.get('weekly_pickup')
        one_time_pickup = request.POST.get('one_time_pickup')
        new_customer = Customer(name=name, user=user, zip_code=zip_code, weekly_pickup=weekly_pickup,street_address=street_address, one_time_pickup=one_time_pickup)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))

    else:
      
        return render(request, 'customers/create.html')
   

def detail(request):
    user = request.user
    logged_in_customer = Customer.objects.get(user=user)
    context = { 
        'logged_in_customer': logged_in_customer
    }    
    return render(request, 'customers/detail.html', {'customer': logged_in_customer})

def change_pickup(request):
     user = request.user
     customer = Customer.objects.get(user=user)
     if request.method == 'POST':
        change_pickup = request.POST.get('change_pickup')
        customer.weekly_pickup = change_pickup
        customer.save()
        return HttpResponseRedirect(reverse('customers:detail'))

     else:
        context ={'customer':customer}
        return render(request, 'customers/change_pickup.html', context)

def suspend(request):
     user = request.user
     customer = Customer.objects.get(user=user)
     if request.method == 'POST':
         customer.suspend_start = request.POST.get('suspend_start')
         customer.suspend_end = request.POST.get('suspend_end')
         customer.save()
         return HttpResponseRedirect(reverse('customers:detail'))
     else:
        context ={'customer':customer}
        return render(request, 'customers/suspend.html',context)

def pickup(request):
     user = request.user
     customer = Customer.objects.get(user=user)
     if request.method == 'POST':
         customer.one_time_pickup = request.POST.get('one_time_pickup')
         customer.save()
         return HttpResponseRedirect(reverse('customers:detail'))
     else:
        context ={'customer':customer}
        return render(request, 'customers/pickup.html',context)

# def delete(request):
#     user = request.user
#     customer = Customer.objects.get(user=user)
#     customer.delete()
#     return HttpResponseRedirect(reverse('players:detail'))

    # , suspend_start, suspend_end, one_time_pickup