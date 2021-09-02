from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Employee
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all
    user =request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customers = apps.get_model('customers.Customer')
    all_customers = Customers.objects.all()
    two_date = date.today()
    this_day = str(date.today())
    weekday = request.POST.get('day_of_the_week')
    todays_customers = []
    for customer in all_customers: 
        customer_suspend_start = str(customer.suspend_start)
        customer_suspend_end = str(customer.suspend_end)
        if  this_day < customer_suspend_start or this_day > customer_suspend_end:     
            if customer.zip_code == logged_in_employee.zip_code and (customer.weekly_pickup == weekday or customer.one_time_pickup == weekday) :
                todays_customers.append(customer)

    try: 
        logged_in_employee = Employee.objects.get(user=user)
        
        
    except:
        return HttpResponseRedirect(reverse('employees:create'))

    context = { 'todays_customers' : todays_customers,
                'weekday': weekday}
    return render(request,'employees/index.html', context)


 
    

def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name = name, user = user, zip_code = zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


def confirm(request, user_id):
    Customers = apps.get_model('customers.Customer')
    customer_charge = Customers.objects.get(pk = user_id)
    context = { 'new_balance': customer_charge}
    if request.method == 'POST':
        if customer_charge.balance == None:
            customer_charge.balance = 0
        customer_charge.balance += 4
        customer_charge.save()
        return HttpResponseRedirect(reverse('employees:daily_view'))
    else:
        return render(request, 'employees/confirm.html', context)

def daily_route(request):
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customers = apps.get_model('customers.Customer')
    all_customers = Customers.objects.all()
    two_date = date.today()
    this_day = str(date.today())
    weekday = request.POST.get('day_of_the_week')
    todays_customers = []

    for customer in all_customers: 
        customer_suspend_start = str(customer.suspend_start)
        customer_suspend_end = str(customer.suspend_end)
        if  this_day < customer_suspend_start or this_day > customer_suspend_end:     
            if customer.zip_code == logged_in_employee.zip_code and (customer.weekly_pickup_day == weekday or customer.one_time_pickup == weekday) :
                todays_customers.append(customer)

    context = { 'todays_customers' : todays_customers,
                'weekday': weekday}
    return render(request, 'employees/day_route.html', context)        