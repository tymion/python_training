import logging

from django.forms import Form, ModelForm, CharField, TimeField, IntegerField, ChoiceField, ModelChoiceField
from django.core.validators import MaxValueValidator, MinValueValidator

from address.forms import AddressField

from .models import Category, DayOfTheWeek, Coach, Country

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

class EditCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_text']
        labels = {
            'category_text': 'Edit category',
        }

class AddDayOfTheWeekForm(ModelForm):
    index_int = IntegerField(label = 'Day number:', max_value = 6, min_value = 0)

    class Meta:
        model = DayOfTheWeek
        fields = ['day_text', 'index_int']
        labels = {
            'day_text': 'Day name:',
        }

class ListDayOfTheWeekForm(Form):
    days_list = ModelChoiceField(queryset = DayOfTheWeek.objects.all().values_list('index_int', 'day_text', named=False), empty_label = "")

class EditDayOfTheWeekForm(ModelForm):
    index_int = IntegerField(label = 'Edit day number:', max_value = 6, min_value = 0)

    class Meta:
        model = DayOfTheWeek
        fields = ['day_text', 'index_int']
        labels = {
            'day_text': 'Edit day name:',
        }

class TestForm(Form):
    coachAddress_address = AddressField()

class AddCoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = [
                'name_text',
                'surname_text',
                'alias_text',
                'coachAddress_address',
                'description_text',
                'category_array',
        ]
        labels = {
            'name_text': 'Name:',
            'surname_text': 'Surname:',
            'alias_text': 'Alias:',
            'coachAddress_address': 'Address:',
            'description_text': 'Description:',
            'category_array': 'Categories:',
        }
        fields_classes = {
            'coachAddress_address': AddressField
        }

class AddCountryForm(ModelForm):
    class Meta:
        model = Country
        fields = [ 'name_text', 'code_int' ]
        labels = {
                'name_text': 'Kraj:',
                'code_int': 'Kod:',
        }
