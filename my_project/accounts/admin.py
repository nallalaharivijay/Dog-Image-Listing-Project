from django.contrib import admin
from .models import ImageList

class ImageListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'user__username')     # Fields to search by in the admin panel
    list_filter = ('user', 'created_at')           # Filters to apply in the admin panel

# Registering the model using admin.site.register()
admin.site.register(ImageList, ImageListAdmin)
