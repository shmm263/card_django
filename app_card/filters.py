import django_filters
from .models import Patient,MedExamination

class PosteFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    addr_city = django_filters.CharFilter(lookup_expr='icontains')
    phone_mobile = django_filters.CharFilter(field_name='phone_mobile', lookup_expr='icontains')
    inn = django_filters.CharFilter(field_name='inn', lookup_expr='icontains')
    class Meta:
       model = Patient
       fields = {'first_name', 'addr_city', 'phone_mobile','inn'}

class PosteFilter1(django_filters.FilterSet):
    patient_status = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
       model = MedExamination
       fields = {'patient_status'}