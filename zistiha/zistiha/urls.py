"""zistiha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from azmoon import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^order/exam/listmultiple',views.examslistmultiple),
    url(r'^order/exam/list',views.examslist),
    url(r'^order/exam/pay',views.payexam), 

    url(r'^take/exam/form',views.getexamform),
    url(r'^take/exam/',views.takeexam),      
    url(r'^take/exam/resultsform',views.resultsform),    
    url(r'^take/exam/results',views.getresults), 
    url(r'^submit-exam/',views.submitexam),

    url(r'^order/course/single/',views.courseenrolsingle),
    url(r'^order/course/multiple/',views.courseenrolmultiple),
    url(r'^order/course/pay',views.coursepayment), 

    url(r'^order/hotel/reserve',views.hotelreserve), 
    url(r'^order/hotel/form',views.hotelreserveform), 
    url(r'^order/hotel/pay',views.hotelpayment), 
    
    url(r'^order/print',views.printreport), 
    url(r'^order/testprint',views.testprint), 





]
