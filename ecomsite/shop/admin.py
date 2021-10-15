from django.contrib import admin
from .models import Products, Orders

# Register your models here.
admin.site.site_header = "Proiect Platforma E-commerce"
admin.site.site_title = "Magazin de bijuterii"
admin.site.index_title = "Administrare Magazin"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price',
                    'category', 'description', 'image')
    search_fields = ('description', 'category', 'name')


admin.site.register(Products, ProductAdmin)
admin.site.register(Orders)
