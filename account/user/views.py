from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
def adminsignup(request):
    z='ADMIN'
    if request.method == 'POST':

        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        p=request.POST.get('password')
        c_p=request.POST.get('confirm_password')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        if p!=c_p  :
            messages.warning(request,'PASSWORD IS MISMATCH ENTER CORRECT ONE')
            return redirect('adminsignup')
        else:
            if User.objects.filter(username=u).exists():
                messages.info(request,'USERNAME EXIST')
                return redirect('adminsignup')
            else:
                user=User.objects.create_user(username=u,password=p,first_name=f.title(),last_name=l.title(),email=e,Is_Admin=True,mobile_number=m)
                user.save()
                a=Administator.objects.create(user=user)
                a.save()
                messages.success(request,'YOU HAVE SUCCESSFULLY SIGNED UP PLEASE LOGIN')
                return redirect('login')
    return render(request,'signup.html',{'z':z})

def managersignup(request):
    z='MANAGER'
    if request.method=='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        p=request.POST.get('password')
        c_p=request.POST.get('confirm_password')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        if p!=c_p  :
            messages.warning(request,'PASSWORD IS MISMATCH ENTER CORRECT ONE')
            return redirect('managersignup')
        else:
            if User.objects.filter(username=u).exists():
                messages.info(request,'USERNAME EXIST')
                return redirect('managersignup')
            else:
                user=User.objects.create_user(username=u,password=p,first_name=f.title(),last_name=l.title(),email=e,Is_Manager=True,mobile_number=m)
                user.save()
                a=Manager.objects.create(user=user)
                a.save()
                messages.success(request,'YOU HAVE SUCCESSFULLY SIGNED UP PLEASE LOGIN')
                return redirect('login')
    return render(request,'signup.html',{'z':z})
def hrsignup(request):
    z='HR'
    if request.method=='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        p=request.POST.get('password')
        c_p=request.POST.get('confirm_password')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        if p!=c_p  :
            messages.warning(request,'PASSWORD IS MISMATCH ENTER CORRECT ONE')
            return redirect('adminsignup')
        else:
            if User.objects.filter(username=u).exists():
                messages.info(request,'USERNAME EXIST')
                return redirect('adminsignup')
            else:
                user=User.objects.create_user(username=u,password=p,first_name=f.title(),last_name=l.title(),email=e,Is_Hr=True,mobile_number=m)
                user.save()
                a=Hr.objects.create(user=user)
                a.save()
                messages.success(request,'YOU HAVE SUCCESSFULLY SIGNED UP PLEASE LOGIN')
                return redirect('login')
    return render(request,'signup.html',{'z':z})


def login(request):
    if request.method=='POST':
        u=request.POST.get('username')
        p=request.POST.get('password')
        user=auth.authenticate(username=u,password=p)
        if user is not None and user.Is_Admin:
            auth.login(request,user)
            return redirect('adminview')           
        elif user is not None and user.Is_Manager:
             auth.login(request,user)
             return redirect('managerview')
        elif user is not None and user.Is_Hr:
            auth.login(request,user)
            return redirect('hrview')
        elif user is not None and user.Is_Employee and user.employee.is_approved :
            auth.login(request,user)
            return redirect('employeeview')
        else:
            messages.warning(request,'INVALID LOGIN')
            return redirect('login')
    return render(request,'login.html')
def home(request):
    return render(request,'dashboard.html')

from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def adminview(request):
    if 'profile' in request.POST:
     a=Administator.objects.get(user=request.user)  
     return render (request,'profile.html',locals())
    elif 'approveemployee' in request.POST:
      return redirect('apem')
    elif 'employeedata' in request.POST:
      a=Employee.objects.all()
      return render(request,'dilli.html',{'a':a})
    elif 'logout' in request.POST:
       return redirect('logout')
    elif 'hrdata' in request.POST:
        a=Hr.objects.all()
        return render(request,'hrdata.html',locals())
    elif 'managerdata' in request.POST:
        a=Manager.objects.all()
        return render(request,'managerdata.html',locals())
    elif 'search' in request.POST:
     query=request.POST.get('searches')
     print(query)
     if query  :
        a=Employee.objects.filter(Q(user__username__icontains=query))and Employee.objects.filter(is_approved=True)
     else:
        messages.info(request,'user Not found')
        return redirect('adminview')

     return render(request,'adminview.html',locals())  
    elif 'role' in request.POST:
        return redirect('role')

    return render (request,'adminview.html')

@login_required
def managerview(request):
    if 'profile' in request.POST:
        a=Manager.objects.get(user=request.user)
        return render (request,'profile.html',locals())
    elif 'addemployee' in request.POST:
        return redirect('addemployee')
    elif 'employeedata' in request.POST:
        a=Employee.objects.all()
        return render(request,'data.html',{'a':a})
    elif 'logout' in request.POST:
         return redirect('logout')
    elif 'search' in request.POST:
        query=request.POST.get('searches')
        print(query)
        if query  :
         a=Employee.objects.filter(Q(user__username__icontains=query)) and Employee.objects.filter(is_approved=True)
        else:
         messages.info(request,'user Not found')
         return redirect('managerview')
        return render (request,'managerview.html',locals())
    return render (request,'managerview.html',locals())


@login_required
def hrview(request):
 if 'profile' in request.POST:
    a=Hr.objects.get(user=request.user)
    return render (request,'profile.html',locals())
 elif 'employeedata' in request.POST:
    a=Employee.objects.all()
    return render(request,'data.html',{'a':a})
 elif 'logout' in request.POST:
    return redirect('logout')
 elif 'leave' in request.POST:
    return redirect('approveleave')
 elif 'search' in request.POST:
    query=request.POST.get('searches')
    print(query)
    if query  :
        a=Employee.objects.filter(Q(user__username__icontains=query)) and Employee.objects.filter(is_approved=True)
    else:
        messages.info(request,'user Not found')
        return redirect('hrview')

    return render(request,'hrview.html',locals()) 
 return render (request,'hrview.html')

@login_required
def employeeview(request):
 if 'profile' in request.POST:
    a=Employee.objects.get(user=request.user)
    return render (request,'profile.html',locals())
 elif 'logout' in request.POST:
    return redirect('logout')
 elif 'leave_request' in request.POST :
    return redirect('leave')
 elif 'view' in request.POST :
    leaves=leaverequest.objects.filter(user=request.user.employee)
    print(leaves)
    return render(request,'view.html',locals())
   
 return render (request,'employeeview.html')
@login_required
def addemployee(request):
    if request.method=='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        p=request.POST.get('password')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        g=request.POST.get('gender')
        s=request.POST.get('salary')
        d=request.POST.get('dob')
        dp=request.POST.get('d')
       
        
        if User.objects.filter(username=u).exists():
                messages.info(request,'EMPLOYEE EXIST')
                return redirect('addemployee')
        else:
                user=User.objects.create_user(username=u,password=p,first_name=f.title(),last_name=l.title(),email=e,Is_Employee=True,mobile_number=m)
                a=Employee.objects.create(user=user,salary=s,gender=g,dob=d,department=dp)
                a.save()
                user.save()
                
                messages.success(request,'EMPLOYEE CREATED')
                return redirect('adminview')

    return render(request,'addemployee.html')
  
def logout(request):
    auth.logout(request)
    messages.success(request,'You Session expired ')

    return redirect('home')
#official Edit
@login_required
def edit(request,id):
    i=Employee.objects.get(user__id=id)
    if request.method =='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        s=request.POST.get('salary')
        lo=request.POST.get('address')
        d=request.POST.get('department')
        edit1=User.objects.get(username=u)

        edit=Employee.objects.get(user__username=u)
        edit1.first_name=f
        edit1.username=u
        edit1.last_name=l
        edit.department=d
        edit.address=lo
        edit1.mobile_number=m
        edit.salary=s
        edit1.save()
        edit.save()
        return redirect('hrview')
    return render(request,'editemployee.html',{'i':i})

@login_required
def editprofile(request):
    a=User.objects.get(username=request.user)
    print(a)
    if request.method =='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        edit=User.objects.get(username=u)
        edit.username=u
        edit.first_name=f.title()
        edit.last_name=l.title()
        edit.email=e
        edit.mobile_number=m
        edit.save()
        if a.Is_Manager:
         return redirect('managerview')
        elif a.Is_Admin:
            return redirect('adminview')
        elif a.Is_Hr:
            return redirect('hrview')


    return render(request,'hredit.html',{'a':a})
#Personal Edit
@login_required
def profileedit(request):
    i=Employee.objects.get(user__username=request.user)
    print(i)
    if request.method =='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        s=request.POST.get('salary')
        d=request.POST.get('department')
        b=request.POST.get('bank')
        i=request.POST.get('ifsc')
        a=request.POST.get('account')
        db=request.POST.get('date')
        ln=request.POST.get('language')
        edit1=User.objects.get(username=u)
        edit=Employee.objects.get(user__username=u)
        edit1.first_name=f
        edit1.last_name=l
        edit1.mobile_number=m
        edit.bank_name=b
        edit.account_no=a
        edit.dob=db
        edit.language=ln
        edit.ifsc_code=i
        edit1.save()
        edit.save()
        return redirect('employeeview')
    return render (request,'profileedit.html',{'i':i})
@login_required
def leave(request):
    request.user=Employee.objects.get(user=request.user)
    if request.method == 'POST':
        f=request.POST.get('from_date')
        t=request.POST.get('to_date')
        ty=request.POST.get('leave_type')
        r=request.POST.get('reason')
        s=leaverequest.objects.create(from_date=f,to_date=t,leave_type=ty,reason=r,user=request.user)
        s.save()
        return redirect('employeeview')
    return render (request,'leave.html')


#LEAVES
@login_required
def approvedleave(request):
    a=leaverequest.objects.all()
    return render(request,'acceptleave.html',locals())
@login_required      
def approve(request,id):
    leaves = leaverequest.objects.get(id=id)
    leaves.is_approved = True
    leaves.save()
    return redirect('approveleave')
@login_required
def reject(request,id):
    leaves = leaverequest.objects.get(id=id)
    leaves.is_rejected = True
    leaves.save()
    return redirect('approveleave')
#ADMIN EDITED
@login_required
def hreditable(request,id)  :
    i=Hr.objects.get(user__id=id)
    if request.method =='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        i=request.POST.get('emp_id')
        d=request.POST.get('dept')
        edit1=User.objects.get(id=id)
        print(edit1)
        edit=Hr.objects.get(user__id=id)
        edit1.username=u
        edit1.first_name=f.title()
        edit1.last_name=l.title()
        edit1.email=e
        edit1.mobile_number=m
        edit.department=d
        edit.emp_id=i
        edit1.save()
        edit.save()
        return redirect('adminview')
    return render (request,'hreditable.html',locals())


@login_required
def manageredit(request,id):
    i=Manager.objects.get(user__id=id)
    if request.method =='POST':
        f=request.POST.get('firstname')
        u=request.POST.get('username')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        m=request.POST.get('mobile_number')
        i=request.POST.get('emp_id')
        d=request.POST.get('dept')
        edit1=User.objects.get(username=u)
        edit=Manager.objects.get(user__username=u)
        edit1.first_name=f.title()
        edit1.last_name=l.title()
        edit1.email=e
        edit1.mobile_number=m
        edit.department=d
        edit.emp_id=i
        edit1.save()
        edit.save()
        print(l)
        return redirect('adminview')
    return render (request,'manageredit.html',{'i':i})
 
def rolex(request,id):
    i=Employee.objects.get(user__id=id)
    if request.method =='POST':
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        e=request.POST.get('email')
        u=request.POST.get('username')
        m=request.POST.get('mobile_number')
        z=request.POST.get('ifsc')
        a=request.POST.get('account')
        db=request.POST.get('date')
        b=request.POST.get('bank')
        ln=request.POST.get('language')
        s=request.POST.get('salary')
        lo=request.POST.get('address')
        d=request.POST.get('department')
        edit1=User.objects.get(id=id)

        edit=Employee.objects.get(user__id=id)
        edit1.first_name=f
        edit1.username=u
        edit1.last_name=l
        edit.email=e
        edit.department=d
        edit.address=lo
        edit.dob=db
        edit.ifsc_code=z
        edit.bank_name=b
        edit.language=ln
        edit.account_no=a
        edit1.mobile_number=m
        edit.salary=s
        edit1.save()
        edit.save()
        return redirect('adminview')
    return render(request,'rolex.html',{'i':i})



@login_required
def role(request):
    a=Employee.objects.all()
    if request.method =='POST':
            u=request.POST.get('username')
            r=request.POST.get('role')
            a=Employee.objects.get(user__username=u)
            a.role=r
            a.save()
            return redirect('adminview')
    return render(request,'role.html',locals())

@login_required
def apem(request):
    a=Employee.objects.all()
    return render(request,'apem.html',locals())
@login_required
def approveemployee(request,id):
    a=Employee.objects.get(user__id=id)
    a.is_approved=True
    a.save()
    return redirect('apem')
@login_required
def rejectemployee(request,id):
    a=Employee.objects.get(user__id=id)
    a.is_rejected=True
    a.save()
    return redirect('apem')






















