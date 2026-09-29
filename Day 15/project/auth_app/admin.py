from django.contrib import admin
from auth_app.models import *

admin.site.register(AbstractModel)  #admin.site.register([Model1, Model2])

admin.site.register(ProductModel)
