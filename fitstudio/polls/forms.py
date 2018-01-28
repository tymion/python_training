from django import forms
from .models import Category

class TermForm(forms.Form):
#    day_array = 
    time_start = forms.TimeField()
    time_end = forms.TimeField()

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_text']
        labels = {
            'category_text': 'Add category',
        }

class ListCategoryForm(forms.Form):
    categories_list = forms.ModelChoiceField(queryset=Category.objects.all().values_list('category_text', flat=True), empty_label="")
