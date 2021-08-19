from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class ArtUserAdmin(UserAdmin):
    list_display = ('username', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Permission', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1','password2' ),
        }),
    )
    readonly_fields = ('date_joined',)