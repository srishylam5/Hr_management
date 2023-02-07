"""hrms_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminsignup/',views.adminsignup,name='adminsignup'),
    path('managersignup/',views.managersignup,name='managersignup'),
    path('hrsignup/',views.hrsignup,name='hrsignup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('adminview/',views.adminview,name='adminview'),
    path('managerview/',views.managerview,name='managerview'),
    path('hrview/',views.hrview,name='hrview'),
    path('employeeview/',views.employeeview,name='employeeview'),
    path('hrview/addemployee/',views.addemployee,name='addemployee'),
    path('logout/',views.logout,name='logout'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('hredit/',views.editprofile,name='hredit'),
    path('profileedit',views.profileedit,name='profileedit'),
    path('leave/',views.leave,name='leave'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('approvedleace/',views.approvedleave,name='approveleave'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('adminview/hreditable/<int:id>',views.hreditable,name='hreditable'),
    path('adminview/manageredit/<int:id>',views.manageredit,name='manageredit'),
    path('adminview/rolex<int:id>/',views.rolex,name='rolex'),
    path('adminview/changerole/',views.role,name='role'),
    path('adminview/employeeapprove/<int:id>/',views.approveemployee,name='approveemployee'),
    path('adminview/employeeapprove/<int:id>/',views.rejectemployee,name='rejectemployee'),
    path('approveemployee/',views.apem,name='apem'),
]
