from django.urls import path, include
from django.contrib import admin

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('new/', views.create, name="accounts:register"),
      
]
# path('account_details/', views.account_details, name="account_details"),
    # path('new_pickup_day/', views.new_pickup_day, name="new_pickup_day"),
    # path('suspend_service/', views.suspend, name='suspend_service'),
    # path('pickup/', views.pickup, name="pickup")  