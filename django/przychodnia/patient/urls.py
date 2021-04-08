from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientList.as_view(), name='patient_list'),
    path('view/<uuid:pk>', views.PatientView.as_view(), name='patient_view'),
    path('new/', views.PatientCreate.as_view(), name='patient_create'),
    path('update/<uuid:pk>', views.PatientUpdate.as_view(), name='patient_update'),
    path('del/<uuid:pk>', views.PatientDelete.as_view(), name='patient_delete'),
    path('edit/', views.UpdatePatient.as_view(), name='patient_edit'),
    ]