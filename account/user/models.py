from django.db import models

from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
import random
from django.utils import timezone
class User(AbstractUser):
    username=models.CharField(max_length=20,unique=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    Is_Admin = models.BooleanField(default=False)
    Is_Manager = models.BooleanField(default=False)
    Is_Hr = models.BooleanField(default=False)
    Is_Employee = models.BooleanField(default=False)
    mobile_number=models.CharField(max_length=13)

user_type=(('Admin','Admin'),('Manager','Manager'),('Hr','Hr'),('Employee','Employee'))

class Administator(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    user_type=models.CharField(choices=user_type,default='Admin',max_length=20)
    emp_id=models.CharField(max_length=20 ,default='ADMIN'+str(random.randrange(100000,999999)))
    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    user_type=models.CharField(choices=user_type,default='Manager',max_length=20)
    emp_id=models.CharField(max_length=20, default='MAN'+str(random.randrange(100000,999999)))
    profile=models.CharField(default='Manager',max_length=20)
    def __str__(self):
        return self.user.username
 

class Hr(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    user_type=models.CharField(choices=user_type,default='Hr',max_length=20)
    emp_id=models.CharField(max_length=20 ,default='HR'+str(random.randrange(100000,999999)))
    dept=models.CharField(default='HR',max_length=20)
    def __str__(self):
        return self.user.username

class Employee(models.Model):
    GENDER = (('male','MALE'),
     ('female', 'FEMALE'),
     ('other', 'OTHER'))
    BANK=(('bank of boroda','BANK OF BARODA'),
    ('union BANK','UNION BANK'),
    ('SBI','STATE BANK OF INDIA'),
    ('axis','AXIS BANK LTD'),
    ('canara bank','CANARA BANK'),
    ('citi bank','CITI BANK'),
    ('HDFC','HDFC BANK'),
    ('icici','ICICI BANK'))
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    dob=models.DateField(max_length=20,null=True)
    user_type=models.CharField(choices=user_type,default='Employee',max_length=20)
    emp_id=models.CharField(max_length=20 ,default='EMP'+str(random.randrange(100000,999999)))
    address = models.TextField(max_length=100, default='')
    gender = models.CharField(choices=GENDER, max_length=10)
    department=models.CharField(max_length=20,null=False)
    joined_date = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=10, default='English')
    bank_name = models.CharField(max_length=25,choices=BANK)
    account_no=models.CharField(max_length=20,null=True)
    ifsc_code=models.CharField(max_length=20,null=True)
    role=models.CharField(max_length=20,null=True)
    salary = models.CharField(max_length=16,default='00,000.00')  
    is_approved=models.BooleanField(null=True,default=False) 
    is_rejected=models.BooleanField(null=True,default=False) 
    def __str__(self):
        return self.user.username


class leaverequest(models.Model):
    user=models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date=models.DateField(null=False)
    to_date=models.DateField(null=False)
    leave_type=models.CharField(max_length=50,null=False)
    reason=models.TextField(max_length=1000,null=False)
    is_approved=models.BooleanField(null=True,default=False)
    is_rejected=models.BooleanField(null=True,default=False)
    def __str__(self):
       return self.leave_type

