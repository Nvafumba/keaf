from django.contrib import admin

from .models import Person, County, District, LeadershipPosition, Leadership

class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'first_name', 'last_name', 'gender', 'email', 'phone_number', 'county', 'district')
    search_fields = ('person_id', 'first_name', 'last_name', 'email')

class CountyAdmin(admin.ModelAdmin):
    list_display = ('county_id', 'county_name')
    search_fields = ('county_name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_id', 'district_name', 'county')
    search_fields = ('district_name', 'county__county_name')

class LeadershipPositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('person', 'position')
    search_fields = ('person__first_name', 'person__last_name', 'position__name')

admin.site.register(Person, PersonAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(LeadershipPosition, LeadershipPositionAdmin)
admin.site.register(Leadership, LeadershipAdmin)
