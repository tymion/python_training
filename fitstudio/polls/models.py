import datetime

from address.models import AddressField

from django.db.models import Model, CASCADE, ForeignKey
from django.db.models import CharField, IntegerField, ManyToManyField, BooleanField, TimeField
from django.db.models import DateField, PositiveSmallIntegerField, PositiveIntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
                )

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

    def __str__(self):
        return self.day_text

class Country(Model):
    name_text = CharField(max_length = 200, unique = True, default = '')
    code_alpha_2_text = CharField(max_length = 2, unique = True, default = '')
    code_alpha_3_text = CharField(max_length = 3, unique = True, default = '')
    code_int = PositiveSmallIntegerField(
            default = 0,
            unique = True,
            validators = [
                MaxValueValidator(999),
                MinValueValidator(1),
                ]
            )

    def __str__(self):
        return self.name_text

class Voivodship(Model):
    name_text = CharField(max_length = 200)
    code_int = PositiveSmallIntegerField(
            default = 0,
            unique = True,
            validators = [
                MaxValueValidator(32),
                MinValueValidator(2),
                validate_even
                ]
            )
    country_key = ForeignKey(Country, on_delete = CASCADE)

    def __str__(self):
        return self.name_text + " (" + str(self.country_key) + ")"

class County(Model):
    name_text = CharField(max_length = 200)
    code_int = PositiveSmallIntegerField(
            default = 0,
            blank = True,
            validators = [
                MaxValueValidator(79),
                MinValueValidator(1),
                ]
            )
    voivodship_key = ForeignKey(Voivodship, on_delete = CASCADE)

    def __str__(self):
        return self.name_text + ", " + str(self.voivodship_key)

class AdministrativeCodeUnitType(Model):
    name_text = CharField(max_length = 200)
    code_int = PositiveSmallIntegerField(
            default = 0,
            unique = True,
            validators = [
                MaxValueValidator(9),
                MinValueValidator(1),
                ]
            )

    def __str__(self):
        return self.name_text

class AdministrativceCommunity(Model):
    name_text = CharField(max_length = 200)
    code_int = PositiveSmallIntegerField(
            default = 0,
            unique = True,
            validators = [
                MaxValueValidator(20),
                MinValueValidator(1),
                ]
            )
    county_key = ForeignKey(County, on_delete = CASCADE)
    unit_type_key = ForeignKey(AdministrativeCodeUnitType, on_delete = CASCADE)

    def __str__(self):
        # TODO custom str according to unit_type_key
        return self.name_text

class PostalCode(Model):
    postal_code_int = PositiveIntegerField(
            default = 0,
            unique = True,
            validators = [
                MinValueValidator(1),
                MaxValueValidator(99999),
                ]
            )

    def __str__(self):
        return '{0:02d}-{1:03d}'.format(self.postal_code_int // 1000, self.postal_code_int % 1000)

class Address(Model):
    community_key = ForeignKey(
            AdministrativceCommunity,
            on_delete = CASCADE,
            blank = True,
            null = True
            )
    street_text = CharField(max_length = 200, default='')
    house_nr_int = PositiveSmallIntegerField(
            default = 0,
            validators = [
                MinValueValidator(1),
                ]
            )
    flat_nr_int = PositiveSmallIntegerField(
            default = 0,
            validators = [
                MinValueValidator(1),
                ]
            )
    postal_code_key = ForeignKey(
            PostalCode,
            on_delete = CASCADE,
            blank = True,
            null = True
            )

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
