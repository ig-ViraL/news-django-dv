from django.contrib import admin
from .models import category
from .models import products

class categorydisplay(admin.ModelAdmin):
    list_display = ('Category',)

class productdisplay(admin.ModelAdmin):
    list_display = ('Category','Product','Price','Quantity','Description')

    def category(self,instance):
        return instance.category

# Register your models here.
admin.site.register(category,categorydisplay)
admin.site.register(products,productdisplay)