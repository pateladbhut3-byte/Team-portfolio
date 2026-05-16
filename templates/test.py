{% comment %} model

from django.db import models
class Form(models.Model):
    student_first_name=models.CharField(max_length=30)
    student_middle_name=models.CharField(max_length=30)
    student_last_name=models.CharField(max_length=30)
    student_father_name=models.CharField(max_length=30)
    student_mother_name=models.CharField(max_length=30)
    student_mobile_no=models.CharField(max_length=15)
    student_email=models.EmailField()
    student_aadhar_no=models.CharField(max_length=30)
    student_dob=models.DateField()
    student_gender=models.CharField(max_length=15)
    student_course=models.CharField(max_length=50)
    student_branch=models.CharField(max_length=50)
    student_year=models.CharField(max_length=10)
    student_category=models.CharField(max_length=30)
    student_permanent_addresss=models.TextField()






# Create your models here.


{% endcomment %}



{% comment %} admin



from django.contrib import admin
from form.models import Form
class FormAdmin(admin.ModelAdmin):
    list_display=('student_first_name','student_middle_name','student_last_name','student_father_name','student_mother_name','student_mobile_no','student_email','student_aadhar_no','student_dob',
                  'student_gender','student_course','student_branch','student_year','student_category','student_permanent_addresss')
admin.site.register(Form,FormAdmin)


# Register your models here.{% endcomment %}



{% comment %} app


from django.apps import AppConfig


class FormConfig(AppConfig):
    name = 'form'

{% endcomment %}

{% comment %} 
view

from form.models import Form

{% endcomment %}