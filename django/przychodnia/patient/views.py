from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Pacjent
from .forms import PacjentForm

class PatientList(ListView):
    model = Pacjent
    template_name = "list.html"

class PatientView(DetailView):
    model = Pacjent
    template_name = "view.html"

class PatientCreate(CreateView):
    model = Pacjent
    template_name = "create.html"
    fields = ['imie', 'nazwisko', 'data_zabiegu']
    success_url = reverse_lazy('patient_list')

class PatientUpdate(UpdateView):
    model = Pacjent
    template_name = "create.html"
    fields = ['imie', 'nazwisko', 'data_zabiegu']
    success_url = reverse_lazy('patient_list')

class PatientDelete(DeleteView):
    model = Pacjent
    template_name = "del.html"
    success_url = reverse_lazy('patient_list')

class UpdatePatient(View):
    def get(self, request):
        pacjentUUID = request.GET.get("uuid", "")
        pacjent = Pacjent.objects.get(id=pacjentUUID)
        if pacjent:
            form = PacjentForm(initial={'imie': pacjent.imie, 'nazwisko': pacjent.nazwisko, 'data_zabiegu':pacjent.data_zabiegu})
            return render(request, 'updatePatient.html', {'form':form})
    def post(self, request):
        form = PacjentForm(request.POST)
        if form.is_valid():
            pacjentUUID = request.GET.get("uuid", "")
            pacjent = Pacjent.objects.get(id=pacjentUUID)
            cd = form.cleaned_data
            pacjent.imie = cd['imie']
            pacjent.nazwisko = cd['nazwisko']
            pacjent.data_zabiegu = cd['data_zabiegu']
            pacjent.save()
            messages.success(self.request, "Zmodyfikowano!")
            return render(request, 'updatePatient.html', {'form':form})


