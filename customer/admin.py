from django.contrib import admin
from . models import room,roombooking,contact


class bookAdmin(admin.ModelAdmin):
     list_display = ('name','email','phone','check_in','check_out','room','adults','childs','request',)

class roomAdmin(admin.ModelAdmin):
     list_display = ('image','room_name','details','cost')

class contactAdmin(admin.ModelAdmin):
     list_display = ('name','email','subject','message')
   
# Register your models here.



admin.site.register(room,roomAdmin)
admin.site.register(roombooking,bookAdmin)
admin.site.register(contact,contactAdmin)