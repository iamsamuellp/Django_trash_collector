from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('confirm/', views.confirm, name="confirm"),
    # path('daily_route/', views.daily_route, name="daily_route"),


    
]