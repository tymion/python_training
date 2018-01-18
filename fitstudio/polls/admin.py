from django.contrib import admin

# Register your models here.
from .models import Student, Coach, Term, ActivityTimeTable, ActivityDone, DayOfTheWeek, Category

admin.site.register(Category)
admin.site.register(DayOfTheWeek)
admin.site.register(Student)
admin.site.register(Coach)
admin.site.register(Term)
admin.site.register(ActivityTimeTable)
admin.site.register(ActivityDone)
