from django.urls import path
from .views import SignupView , HomeView , LogunView ,CustomLogoutViews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LogunView.as_view(), name='login'),
    path('logout/', CustomLogoutViews.as_view(), name='logout'),
  
]
