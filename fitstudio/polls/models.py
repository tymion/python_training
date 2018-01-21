from django.db import models
from address.models import AddressField
import datetime

# Create your models here.
class Student(models.Model):
    student_text = models.CharField(max_length=200)

    def __str__(self):
        return self.student_text

class Category(models.Model):
    category_text = models.CharField(max_length=50)

class DayOfTheWeek(models.Model):
    index_int = models.IntegerField(default=0)
    day_text = models.CharField(max_length=50)

class Coach(models.Model):
    name_text = models.CharField(max_length=200)
    surname_text = models.CharField(max_length=200)
    alias_text = models.CharField(max_length=200)
    coachAddress_address = AddressField(on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    category_array = models.ManyToManyField(Category)

class Term(models.Model):
    day_array = models.ManyToManyField(DayOfTheWeek)
    periodic_bool = models.BooleanField(default=False)
    timeStart_time = models.TimeField('time_start')
    timeEnd_time = models.TimeField('time_end')

class ActivityTimeTable(models.Model):
    activity_text = models.CharField(max_length=200)
    coach_key = models.ForeignKey(Coach, on_delete=models.CASCADE)
    maxStudentCnt_int = models.IntegerField(default=0)
    term_key = models.ForeignKey(Term, on_delete=models.CASCADE)
    dateStart_date = models.DateField('date_start', default=datetime.date.today)
    dateEnd_date = models.DateField('date_end', default=datetime.date.today,
            null=True, blank=True)
    category_array = models.ManyToManyField(Category)

class ActivityDone(models.Model):
    activity_key = models.ForeignKey(ActivityTimeTable, on_delete=models.CASCADE)
    coachReplacement_key = models.ForeignKey(Coach, on_delete=models.CASCADE,
            null=True, blank=True)
    date = models.DateField('activity_date', default=datetime.date.today)
    studentCnt_int = models.IntegerField(default=0)

class WorkHours(models.Model):
    day_array = models.ManyToManyField(DayOfTheWeek)
    hourStart_time = models.TimeField()
    hourEnd_time = models.TimeField()
    dateStart_date = models.DateField('work_start_date',
            default=datetime.date.today)
    dateEnd_date = models.DateField('work_end_date',
            default=datetime.date.today, null=True, blank=True)
