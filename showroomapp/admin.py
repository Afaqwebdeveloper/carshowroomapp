from django.contrib import admin
from .models import ShowRoom, Staff, Brand, Model, Engine, Feature, Car

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'get_engine_number', 'get_features')
    list_filter = ('brand',)
    search_fields = ('name', 'brand__name')

    def get_engine_number(self, obj):
        return obj.engine.engine_number
    get_engine_number.short_description = 'Engine Number'

    def get_features(self, obj):
        return ", ".join([feature.name for feature in obj.features.all()])
    get_features.short_description = 'Features'

class CarAdmin(admin.ModelAdmin):
    list_display = ('get_brand', 'model', 'chassis_number', 'get_engine_number')
    list_filter = ('model__brand', 'model__name')
    search_fields = ('chassis_number', 'model__name', 'model__brand__name')

    def get_brand(self, obj):
        return obj.model.brand.name
    get_brand.short_description = 'Brand'

    def get_engine_number(self, obj):
        return obj.model.engine.engine_number
    get_engine_number.short_description = 'Engine Number'

class EngineAdmin(admin.ModelAdmin):
    list_display=('name', 'engine_number')    

admin.site.register(ShowRoom)
admin.site.register(Staff)
admin.site.register(Brand)
admin.site.register(Model, ModelAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(Feature)
admin.site.register(Car, CarAdmin)
