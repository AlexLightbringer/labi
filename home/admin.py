from django.contrib import admin
from .models import Job, Order

admin.site.register(Job)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "client",
        "email",
        "phone",
        "order",
        "file_download_link",
    )

    def file_download_link(self, obj):
        if obj.file_upload:
            return f'<a href="{obj.file_upload.url}" download>Download</a>'
        else:
            return "No file"

    file_download_link.short_description = "File Download Link"


admin.site.register(Order, OrderAdmin)
