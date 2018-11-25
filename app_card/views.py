from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from requests import request

from .models import Patient, MedExamination
from django.views import generic
import datetime
# Create your views here.
from .tables import CurrentTables,MedExaminationsTable
from .filters import PosteFilter, PosteFilter1
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .forms import RenewStatusForm
from django.shortcuts import get_object_or_404

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_patients =  Patient.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_patients': num_patients, },
    )

class PatientListView(generic.ListView):
 model = Patient

class PatientDetailView(generic.DetailView):
 model = Patient
template_name = 'app_card/Patient_detail.html'

#class LoanedPatientByDateListView(generic.ListView):
 #model = Patient
 #template_name = 'app_card/patient_list_enddate.html'


 #def get_queryset(self):
     #start_day = datetime.date.today()
     #end_day = datetime.date.today() + datetime.timedelta(weeks=3)
     #return MedExamination.objects.filter(dat_end__range=(start_day,end_day))


class FilteredPersonListView(SingleTableMixin, FilterView):
     table_class = CurrentTables
     model = Patient
     filterset_class = PosteFilter
     template_name = 'app_card/people.html'


class FilteredPersonListView1(SingleTableMixin, FilterView):
    start_day = datetime.date.today()
    end_day = datetime.date.today() + datetime.timedelta(weeks=3)
    table_class = MedExaminationsTable
    model = MedExamination
    template_name = 'app_card/people1.html'
    filterset_class = PosteFilter1
    queryset = MedExamination.objects.filter(dat_end__range=(start_day, end_day))


#class MedExaminationDetailView(generic.DetailView):
#    model = MedExamination

def medexamination_update_status(request, pk):
    mde_inst = get_object_or_404(MedExamination, pk=pk)
    if request.method == 'POST':
        form = RenewStatusForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_inst.due_back = form.cleaned_data['renewal_date']
            mde_inst.patient_status = form.cleaned_data['renewal_status']
            #mde_inst.date_update= datetime.date.today()
            mde_inst.save()
            return HttpResponseRedirect(reverse('people1'))
    else:
         proposed_renewal_status = mde_inst.patient_status
    #    form = RenewBookForm(initial={'renewal_date': proposed_renewal_status,})
         form = RenewStatusForm(initial={'renewal_status': proposed_renewal_status, })

    return render(request, 'app_card/MedExamination_detail.html', {'form': form, 'mde_inst': mde_inst})