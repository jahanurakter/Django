from django.contrib import admin
from purchases.models import *

admin.site.register([SupplierModel,UserProfileModel,PurchaseModel])
