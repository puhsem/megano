from django.contrib import admin

from .models import ProductTag, ProductImage, Review, ProductShort

admin.site.register(ProductTag)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(ProductShort)
