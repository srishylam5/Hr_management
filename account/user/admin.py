from django.contrib import admin


from .models import *

admin.site.register(User)
admin.site.register(Administator)
admin.site.register(Manager)
admin.site.register(Hr)
admin.site.register(Employee)

admin.site.register(leaverequest)





