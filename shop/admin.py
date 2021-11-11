from django.contrib import admin
from .models import policy, customer, user_policy
# Register your models here.
admin.site.register(policy)
admin.site.register(customer)
admin.site.register(user_policy)
