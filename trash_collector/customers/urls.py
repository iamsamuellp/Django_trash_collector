from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('new/', views.create, name="register"),
    path('detail/', views.detail, name="detail"),
    path('', RedirectView.as_view(url = '/customers/'))
      
]
# path('account_details/', views.account_details, name="account_details"),
    # path('new_pickup_day/', views.new_pickup_day, name="new_pickup_day"),
    # path('suspend_service/', views.suspend, name='suspend_service'),
    # path('pickup/', views.pickup, name="pickup")  