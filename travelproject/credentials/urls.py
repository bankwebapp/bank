
from django.urls import path

from . import views

urlpatterns = [

    path('register',views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name='form'),
    path('done',views.done,name='done'),
    path('gotoform',views.gotoform,name='gotoform')



]