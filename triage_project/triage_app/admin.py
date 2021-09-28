from django.contrib import admin
from .models import (Patient, Vital, VisitForm)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'dob', 'gender', 'created_at',)
    list_filter = ('first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'dob', 'gender')}),
    )

    search_fields = ('first_name',)
    ordering = ('first_name',)
    filter_horizontal = ()


admin.site.register(Patient, PatientAdmin)


class VitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_fk', 'height', 'weight', 'bmi', )
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('height', 'weight',
         'bmi', 'patient_fk',), }),
    )

    search_fields = ()
    ordering = ('bmi',)
    filter_horizontal = ()


admin.site.register(Vital, VitalAdmin)


class VisitFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_fk', 'on_diet',
                    'health_status', 'comments',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('patient_fk', 'on_diet',
         'health_status', 'comments',), }),
    )

    search_fields = ('health_status',)
    ordering = ('patient_fk',)
    filter_horizontal = ()


admin.site.register(VisitForm, VisitFormAdmin)
