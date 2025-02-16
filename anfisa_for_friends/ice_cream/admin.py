from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category
from .models import Topping
from .models import Wrapper
from .models import IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order',
        'price'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order',
        'price'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )


# ...и регистрируем её в админке:
admin.site.register(Category, CategoryAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)
admin.site.empty_value_display = 'Не задано'
