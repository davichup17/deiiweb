from django.contrib import admin

# Register your models here.


from .models import (Country, Province, City, RoadType,
                                  IdentifierType, Client,
                                  ContactData)


class CountryAdmin(admin.ModelAdmin):
    pass


class ProvinceAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ine_code']
    pass


class RoadTypeAdmin(admin.ModelAdmin):
    pass


class IdentifierTypeAdmin(admin.ModelAdmin):
    pass


class ContactDataAdmin(admin.ModelAdmin):
    search_fields = ('interested__identifier', 'interested__name', 'interested__surname1', 'interested__surname2', )


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('identifier', 'name', 'surname1', 'surname2', )
    readonly_fields = ('create_in',)
    exclude = ('contact_data', )



admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(RoadType, RoadTypeAdmin)
admin.site.register(IdentifierType, IdentifierTypeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ContactData, ContactDataAdmin)

