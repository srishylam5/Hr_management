# Generated by Django 4.1.4 on 2023-02-05 04:47

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('Is_Admin', models.BooleanField(default=False)),
                ('Is_Manager', models.BooleanField(default=False)),
                ('Is_Hr', models.BooleanField(default=False)),
                ('Is_Employee', models.BooleanField(default=False)),
                ('mobile_number', models.CharField(max_length=13)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Administator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Hr', 'Hr'), ('Employee', 'Employee')], default='Admin', max_length=20)),
                ('emp_id', models.CharField(default='ADMIN906284', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField(max_length=20)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Hr', 'Hr'), ('Employee', 'Employee')], default='Employee', max_length=20)),
                ('emp_id', models.CharField(default='EMP277656', max_length=20)),
                ('address', models.TextField(default='', max_length=100)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('department', models.CharField(max_length=20)),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(default='English', max_length=10)),
                ('bank_name', models.CharField(choices=[('bank of boroda', 'BANK OF BARODA'), ('union BANK', 'UNION BANK'), ('SBI', 'STATE BANK OF INDIA'), ('axis', 'AXIS BANK LTD'), ('canara bank', 'CANARA BANK'), ('citi bank', 'CITI BANK'), ('HDFC', 'HDFC BANK'), ('icici', 'ICICI BANK')], max_length=25)),
                ('account_no', models.CharField(max_length=20, null=True)),
                ('ifsc_code', models.CharField(max_length=20, null=True)),
                ('role', models.CharField(max_length=20, null=True)),
                ('salary', models.CharField(default='00,000.00', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Hr', 'Hr'), ('Employee', 'Employee')], default='Hr', max_length=20)),
                ('emp_id', models.CharField(default='HR814221', max_length=20)),
                ('dept', models.CharField(default='HR', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Hr', 'Hr'), ('Employee', 'Employee')], default='Manager', max_length=20)),
                ('emp_id', models.CharField(default='MAN927657', max_length=20)),
                ('profile', models.CharField(default='Manager', max_length=20)),
            ],
        ),
    ]
