from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')
    
    try: 
        logged_in_employee = Employee.objects.get(user=user)
        context = { 
        'logged_in_employee': logged_in_employee
    }    
    except:
        return HttpResponseRedirect(reverse('employees:login.html'))
    return render(request,'employees/index.html', context)

def customerdetails(request):
    logged_in_employee = Employee.objects.get(user=user)
    context = { 
        'logged_in_employee': logged_in_employee
    }    
    return render(request,'employees/index.html', context)

