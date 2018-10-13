import datetime
import django_tables2 as tables
from django_tables2 import A

from .models import Patient, MedExamination


class CurrentTables(tables.Table):
    first_name = tables.LinkColumn('patient-detail', args=[A('id')])
    class Meta:
        model = Patient
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        #fields = ('first_name', 'addr_city', 'phone_mobile')
        attrs = {"class": "table-striped table-bordered "}
        per_page: 25


class MedExaminationsTable(tables.Table):
    id = tables.LinkColumn('patient-detail', args=[A('patient_id')])
    patient_status = tables.LinkColumn('renew-status-medexamination', args=[A('id')])
    #patient_status=tables.Column(accessor='patient_status')
    first_name = tables.Column(accessor='patient.first_name')
    last_name = tables.Column(accessor='patient.last_name')
    addr_city = tables.Column(accessor='patient.addr_city')
    phone_mobile = tables.Column(accessor='patient.phone_mobile')
    inn = tables.Column(accessor='patient.inn')
    email=tables.EmailColumn(accessor='patient.email')
    class Meta:
        model=MedExamination
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        fields = ('id','patient_status','first_name','last_name','addr_city','phone_mobile','email','inn','date_medical_examination','dat_end','purpose_medical_examination')
        attrs = {"class": "table-striped table-bordered "}
        per_page: 25

