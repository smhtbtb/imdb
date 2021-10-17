from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import *

app_name = 'customer'
urlpatterns = [
    path('', MyView.as_view(), name='baseview'),

    # Template Views
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer_temp/logout.html'), name='logout'),
    path('register/', register, name='register'),
    # path('change_password/', MyPasswordChangeView.as_view(), name='change_password'),
]
