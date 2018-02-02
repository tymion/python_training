import datetime

from address.models import AddressField

from django.db.models import Model, CASCADE, ForeignKey
from django.db.models import CharField, IntegerField, ManyToManyField, BooleanField, TimeField
from django.db.models import DateField, PositiveSmallIntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(Model):
    student_text = CharField(max_length = 200)

    def __str__(self):
        return self.student_text

class Category(Model):
    category_text = CharField(max_length = 50, unique = True)

class DayOfTheWeek(Model):
    index_int = PositiveSmallIntegerField(
        default = 0,
        unique = True,
        validators = [
                MaxValueValidator(6),
            ]
    )
    day_text = CharField(max_length = 50, unique = True)

class Coach(Model):
    name_text = CharField(max_length = 200)
    surname_text = CharField(max_length = 200)
    alias_text = CharField(max_length = 200, blank = True)
    coachAddress_address = AddressField(on_delete = CASCADE)
    description_text = CharField(max_length = 200, blank = True)
    category_array = ManyToManyField(Category)

class Term(Model):
    day_array = ManyToManyField(DayOfTheWeek)
    periodic_bool = BooleanField(default = False)
    timeStart_time = TimeField('time_start')
    timeEnd_time = TimeField('time_end')

class ActivityTimeTable(Model):
    activity_text = CharField(max_length = 200)
    coach_key = ForeignKey(Coach, on_delete = CASCADE)
    maxStudentCnt_int = IntegerField(default = 0)
    term_key = ForeignKey(Term, on_delete = CASCADE)
    dateStart_date = DateField('date_start', default = datetime.date.today)
    dateEnd_date = DateField(
                'date_end',
                default = datetime.date.today,
                null = True,
                blank = True
            )
    category_array = ManyToManyField(Category)

class ActivityDone(Model):
    activity_key = ForeignKey(ActivityTimeTable, on_delete = CASCADE)
    coachReplacement_key = ForeignKey(
                Coach,
                on_delete = CASCADE,
                null = True,
                blank = True)
    date = DateField(
                'activity_date',
                default = datetime.date.today
            )
    studentCnt_int = IntegerField(default = 0)

class WorkHours(Model):
    day_array = ManyToManyField(DayOfTheWeek)
    hourStart_time = TimeField()
    hourEnd_time = TimeField()
    dateStart_date = DateField(
                'work_start_date',
                default = datetime.date.today
            )
    dateEnd_date = DateField(
                'work_end_date',
                default = datetime.date.today,
                null = True,
                blank = True
            )
