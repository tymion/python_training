import logging

from django.forms import Form, ModelForm, CharField, TimeField, IntegerField, ChoiceField, ModelChoiceField
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Category, DayOfTheWeek

logger = logging.getLogger(__name__)

class TermForm(Form):
    time_start = TimeField()
    time_end = TimeField()

class NameForm(Form):
    your_name = CharField(label = 'Your name', max_length = 100)

class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_text']
        labels = {
            'category_text': 'Add category',
        }

class ListCategoryForm(Form):
    categories_list = ModelChoiceField(queryset = Category.objects.all().values_list('category_text', flat = True), empty_label = "")

class EditCategoryForm(Form):
    edit_category = CharField(label = 'Edit category:', max_length = 100)

class AddDayOfTheWeekForm(ModelForm):
    class Meta:
        model = DayOfTheWeek
        fields = ['day_text', 'index_int']
        labels = {
            'day_text': 'Add day name',
            'index_int': 'day number',
        }

class ListDayOfTheWeekForm(Form):
    choices_list = [(None, '')]
    for day in DayOfTheWeek.objects.all():
        val = str(day.index_int) + ": " + day.day_text
        choices_list.append((val, val))
    days_list = ModelChoiceField(queryset = DayOfTheWeek.objects.all().values_list('index_int', 'day_text', named=False), empty_label = "")
#    days_list = ChoiceField(choices = choices_list)

class EditDayOfTheWeekForm(Form):
    edit_day_text = CharField(label = 'Edit day name:', max_length = 100)
    edit_day_index = IntegerField(label = 'Edit day index:', max_value = 6, min_value = 0)

