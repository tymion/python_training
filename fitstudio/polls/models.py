from django.db import models

# Create your models here.
class Student(models.Model):
    student_text = models.CharField(max_length=200)

    def __str__(self):
        return self.student_text

class Coach(models.Model):
    coach_text = models.CharField(max_length=200)
    alias_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    style_text = models.CharField(max_length=200)

class Term(models.Model):
    days_text = models.CharField(max_length=200)
    timeStart = models.DateTimeField('time_start')
    timeEnd = models.DateTimeField('time_end')

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
