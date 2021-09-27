from django.urls import path, include
from rest_framework import routers
from .views import (PatientViewSet, VisitFormViewSet, VitalViewSet)

router = routers.DefaultRouter()

router.register(r'patients', PatientViewSet)
router.register(r'visit-forms', VisitFormViewSet)
router.register(r'vitals', VitalViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
