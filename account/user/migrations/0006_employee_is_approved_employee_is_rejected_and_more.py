# Generated by Django 4.1.4 on 2023-02-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_leaverequest_is_rejected_alter_administator_emp_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_rejected',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='administator',
            name='emp_id',
            field=models.CharField(default='ADMIN781161', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='EMP765180', max_length=20),
        ),
        migrations.AlterField(
            model_name='hr',
            name='emp_id',
            field=models.CharField(default='HR220005', max_length=20),
        ),
        migrations.AlterField(
            model_name='manager',
            name='emp_id',
            field=models.CharField(default='MAN584503', max_length=20),
        ),
    ]