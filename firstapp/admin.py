from django.contrib import admin

# Register your models here.
from products.models import Product
from users.models import User

admin.site.register(Product)
admin.site.register(User)

