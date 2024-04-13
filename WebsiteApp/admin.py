from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, CartItem

admin.site.register(CartItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=100,
                height=100,
            ))
        else:
            return 'No Image'
