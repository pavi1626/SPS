# # SmartParkingSystem/urls.py

# from django.contrib import admin
# from django.urls import path
# from PS import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', views.home, name='home'),  # Home page
#     path('register/', views.register, name='register'),  # Registration page
#     path('login/', views.login, name='login'),  # Login page
#     path('logout/', views.logout_view, name='logout'),  # Logout
#     path('contact/', views.contact, name='contact'),  # Contact Us page
#     path('', views.firstpage, name='firstpage'),
# ]

 # SmartParkingSystem/urls.py

from django.contrib import admin
from django.urls import path
from PS import views  # Update this to match your actual app name

admin.site.site_header = "Smart Parking System Admin"
admin.site.site_title = "Parking System Portal"
admin.site.index_title = "Parking System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('status/', views.status, name='status'),
    path('', views.firstpage, name='firstpage'),  # Home page
]
