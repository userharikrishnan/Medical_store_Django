from django.urls import path,include
from pharma import views



urlpatterns = [
    path('home', views.home,name='home'),
    path('',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/', views.logout_page,name='logout'),
    path('items/',include('items.urls')),
    path('productsapi/', include('productsapi.urls')),
    
]