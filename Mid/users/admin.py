from django.contrib import admin
from users.models import CustomUser
from users.managers import CustomUserManager
from .forms import CustomUserCreationForm

@admin.register(CustomUser) #первый способ
class UserAdmin(admin.ModelAdmin):
    list_display=('email',)
    list_display_links=('email',)
    list_filter=('email',)
    search_fields=('email',)
# Register your models here.
