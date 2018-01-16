from django.contrib import admin

# Register your models here.
from .models import Question, Student, Coach, Term, ActivityTimeTable, ActivityDone

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Coach)
admin.site.register(Term)
admin.site.register(ActivityTimeTable)
admin.site.register(ActivityDone)
