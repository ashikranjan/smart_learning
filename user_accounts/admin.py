from django.contrib import admin
from user_accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['email', 'created_at', 'updated_at']
    readonly_fields=(
        'password',
    )


admin.site.register(UserProfile, UserProfileAdmin)
