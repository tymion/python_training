from django.db import models
from address.models import AddressField

# Create your models here.
class Student(models.Model):
    student_text = models.CharField(max_length=200)

    def __str__(self):
        return self.student_text

class Coach(models.Model):
    name_text = models.CharField(max_length=200)
    surname_text = models.CharField(max_length=200)
    alias_text = models.CharField(max_length=200)
    address = AddressField(on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    style_text = models.CharField(max_length=200)

class Category(models.Model):
    category_text = models.CharField(max_length=50)

class DayOfTheWeek(models.Model):
    day_text = models.CharField(max_length=50)

class Term(models.Model):
    day_array = models.ManyToManyField(DayOfTheWeek)
    periodic = models.BooleanField(default=False)
    timeStart = models.TimeField('time_start')
    timeEnd = models.TimeField('time_end')

class ActivityTimeTable(models.Model):
    activity_text = models.CharField(max_length=200)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    maxStudentCnt = models.IntegerField(default=0)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    category_text = models.CharField(max_length=200)

class ActivityDone(models.Model):
    activityTimeTeble = models.ForeignKey(ActivityTimeTable, on_delete=models.CASCADE)
    coachReplacement = models.ForeignKey(Coach, on_delete=models.CASCADE)
    date = models.DateTimeField('activity_date')
    studentCnt = models.IntegerField(default=0)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
