from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student
from fees.admin import FeesInline
from django.http import HttpResponse
import csv
from import_export.admin import ImportExportModelAdmin
from fees.resources import StudentResource
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class StudentAdmin(UserAdmin):
    list_display = ('code', 'username', 'school', 'grade', 'study_paid', 'study_status', 'bus_paid', 'bus_status','last_login')
    search_fields = ('code', 'username')
    readonly_fields = ( 'study_status','bus_status', 'date_joined','last_login')

    # filter_horizontal = ()
    list_filter = ('school','grade', 'bus_active', 'is_staff', 'is_active')
    fieldsets = (
        (None, { 'fields': ('code', 'username', ('school', 'grade'),'password')}),
        ('المصروفات الدراسية', {'fields': (('payment_1', 'payment_2'),('study_paid','study_status'), 'message')}),
        ('إشتراك الباص', {'fields': ( 'bus_active', ('bus_fees', 'bus_paid', 'bus_status'),'old_bus',('area', 'adress'))}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'groups', 'user_permissions')}),
                 )
    resource_class = StudentResource

    def export_bus(self, request, queryset):

        meta = self.model._meta
        # field_names = [field.name for field in meta.fields]
        field_names = ['code', 'username', 'school', 'grade', 'old_bus', 'area', 'adress']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=bus.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_bus.short_description = "Bus Data"



    def export_student(self, request, queryset):

        meta = self.model._meta
        # field_names = [field.name for field in meta.fields]
        field_names = ['code', 'username', 'school', 'grade']
        response = HttpResponse(content_type='text/csv')
        ressponse['Content-Disposition'] = 'attachment; filename=Students.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_student.short_description = "تصدير بيانات الطلبة"



    actions = ["export_bus", "export_student"]

    inlines = [FeesInline]


admin.site.register(Student, StudentAdmin)

admin.site.site_header = "Manarat Al Farouk Islamic Language School"
