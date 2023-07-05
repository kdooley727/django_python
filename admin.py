from django.contrib import admin
from .models import Product
from .models import Member
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image_url')


admin.site.register(Product)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'email')


admin.site.register(Member)
