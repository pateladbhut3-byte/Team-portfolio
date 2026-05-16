
from django.contrib import admin
from form.models import Form

class FormAdmin(admin.ModelAdmin):
    list_display=('student_first_name','student_middle_name','student_last_name','student_father_name','student_mother_name','student_mobile_no','student_email','student_aadhar_no','student_dob',
                  'student_gender','student_course','student_branch','student_year','student_category','student_permanent_addresss')
admin.site.register(Form,FormAdmin)
