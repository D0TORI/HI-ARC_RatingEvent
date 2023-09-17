from django.contrib import admin

# Register your models here.
from .models import RatedUser

# Register your models here.
@admin.register(RatedUser)
class ShowUser(admin.ModelAdmin):
    list_display = (
        'username',
        'seasonStartRating',
        'userrating',
        'userdiv',
        'create_date',
    )
