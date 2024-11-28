from django.contrib import admin
from .models import ImageList, CustomUser
from django.contrib.auth.admin import UserAdmin
class ImageListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'user__username')     # Fields to search by in the admin panel
    list_filter = ('user', 'created_at')           # Filters to apply in the admin panel

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_permissions')}),
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'role', 'user_permissions')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk=request.user.pk)

    def has_view_permission(self, request, obj=None):
        if obj and obj.pk == request.user.pk:
            return True
        return super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        if obj and obj.pk == request.user.pk:
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.pk == request.user.pk:
            return False
        return super().has_delete_permission(request, obj)

# Registering the models using admin.site.register()
admin.site.register(ImageList, ImageListAdmin)
admin.site.register(CustomUser, CustomUserAdmin)