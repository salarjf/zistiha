from django.contrib import admin

# Register your models here.
from .models import Exam,ExamOrder,Bonus,Course

admin.site.register(Exam)
admin.site.register(ExamOrder)
admin.site.register(Bonus)
admin.site.register(Course)