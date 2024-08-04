from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.register(User)

admin.site.site_header = 'Habit Tracker'
admin.site.site_title = 'Habit Tracker'
admin.site.index_title = 'Habit Tracker'


class HabitUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(User, HabitUserAdmin)


class HabitPermissionAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


admin.site.register(Group, HabitPermissionAdmin)

