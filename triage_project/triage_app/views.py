from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response as APIResponse
from .models import (Patient, Vital, VisitForm)


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name',
                  'dob', 'gender', 'created_at',)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class VitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vital
        fields = ('id', 'patient_fk', 'height',
                  'weight', 'bmi', )


class VitalViewSet(viewsets.ModelViewSet):
    queryset = Vital.objects.all()
    serializer_class = VitalSerializer


class VisitFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitForm
        fields = ('id', 'patient_fk',
                  'health_status', 'on_diet', 'comments',)


class VisitFormViewSet(viewsets.ModelViewSet):
    queryset = VisitForm.objects.all()
    serializer_class = VisitFormSerializer
