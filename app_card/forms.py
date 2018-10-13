from django import forms
from .models import Patient,MedExamination
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit #,ButtonHolder

class PosteListFormHelper(FormHelper):
    model = Patient
    form_tag = False
    form_style = 'inline'
    layout = Layout(
        'first_name',
        'addr_city',
        'phone_mobile',
        'inn',
        Submit('submit', 'Filtrer'),
    )

class RenewStatusForm(forms.Form):
    status_choices = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )
    renewal_status = forms.ChoiceField(label='Новий статус',choices=status_choices)
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_status']
        # Помните, что всегда надо возвращать "очищенные" данные.
        return data

