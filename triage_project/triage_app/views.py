from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response as APIResponse
from django.utils.timezone import now
from .models import (Patient, Vital, VisitForm)


class PatientSerializerBrief(serializers.ModelSerializer):
    vitals = serializers.SlugRelatedField(
        queryset=Vital.objects.all().reverse(),
        many=True,
        slug_field='bmi')

    age = serializers.SerializerMethodField(method_name='get_age')

    def get_age(self, obj):
        days = (now().date() - obj.dob).days
        years = days//365 
        age = str(years)+'y '
        months = (days % 365)//30
        if months != 0:
            age += str(months)+'m'
        return age

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name',
                  'dob', 'vitals', 'age','phone_number')


class PatientViewSetBrief(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PatientSerializerBrief


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name',
                  'dob', 'gender', 'created_at',)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vital
        fields = ('id', 'patient_fk', 'height',
                  'weight', 'bmi', )


class VitalViewSet(viewsets.ModelViewSet):
    queryset = Vital.objects.all()
    serializer_class = VitalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VisitFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitForm
        fields = ('id', 'patient_fk',
                  'health_status', 'on_diet', 'comments',)


class VisitFormViewSet(viewsets.ModelViewSet):
    queryset = VisitForm.objects.all()
    serializer_class = VisitFormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
