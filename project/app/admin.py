from django.contrib import admin
from .models import Student,Aadhar

# Register your models here.

# admin.site.register(Student)
# admin.site.register(Aadhar)

class AadharAdmin(admin.ModelAdmin):
    list_display=['id','aadhar']
admin.site.register(Aadhar,AadharAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','aadhar','stu_name','stu_contact','stu_email']
admin.site.register(Student,StudentAdmin)
