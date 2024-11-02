from django.contrib import admin

from .models import Patient
from .models import MedicalRecord

admin.site.register(Patient)
admin.site.register(MedicalRecord)
