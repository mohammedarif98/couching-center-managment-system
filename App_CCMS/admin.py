from django.contrib import admin
from App_CCMS.models import *


# Register your models here.

@admin.register(User_Registration_Model)
class RegistrationDetailAdmin(admin.ModelAdmin):
    list_display=('id','User_Forgn','User_Gender','User_Photo','User_Contact','User_Address',)


@admin.register(Course_Model)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fee','About_Course','Duration','BG_Image',)