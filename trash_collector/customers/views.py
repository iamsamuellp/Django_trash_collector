from trash_collector.customers.apps import CustomersConfig
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
from trash_collector import Customer

# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    login_customer = Customer.objects.all()
    context = {
        'login_customer': login_customer
    }

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('customers:register'))
    return render, 'customers/index.html', context

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.ForeignKey('accounts.User', blank=True, null=True, on_delete=request.CASCADE)
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup = request.POST.get('weekly_pickup')
        one_time_pickup = request.POST.get('one_time_pickup')
        new_customer = CustomersConfig(name=name, address=address, zip_code=zip_code, weekly_pickup=weekly_pickup, one_time_pickup=one_time_pickup)
        new_customer.save()
    else:
        Customer = apps.get_model('customers.Customers')
        all_customers = Customer.objects.all()
        return render(request, 'customers/create.html', {'all_customers': all_customers})
    print(user)
    return render(request, 'customers/index.html')

def detail(request, customer_id):
    customer_from_db = Customer.objects.get(pk=customer_id)
    return render(request, 'customers/detail.html', {'customer_from_db'})

