from django.contrib import admin
from .models import department,lecture,student
#admin.site.register(department)
@admin.register(department)
class departmentadmin(admin.ModelAdmin):
    list_dispaly=['id','dep']
    
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=['id','dep','name','rollno']
admin.site.register(lecture)


#admin.site.register(student)


