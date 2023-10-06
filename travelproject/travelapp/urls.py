
from django.urls import path

from . import views

urlpatterns = [

    path('',views.demo, name='demo'),
    # path('add/',views.addition, name='addition')
    # path('about/',views.aboutfn,name='about'),
    # path('details/',views.detailsfn,name='details')

]