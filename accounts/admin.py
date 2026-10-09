from django.contrib import admin
from .models import UserDetails, VendorDetails


admin.site.register(UserDetails)


@admin.register(VendorDetails)
class VendorDetailsAdmin(admin.ModelAdmin):

    list_display = (
        'RestruntName',
        'lic_no',
        'Gst_no',
        'res_email',
        'res_phone',
        'is_approved',
    )

    list_editable = (
        'is_approved',
    )

    list_filter = (
        'is_approved',
    )

    search_fields = (
        'RestruntName',
        'lic_no',
        'Gst_no',
        'res_email',
    )