from django.urls import path, include
from rest_framework import routers
from .views import (PatientViewSet, VisitFormViewSet,
                    VitalViewSet, PatientViewSet2,)

router = routers.DefaultRouter()


router.register(r'patient-short', PatientViewSet2, basename='patient-short')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'visit-forms', VisitFormViewSet)
router.register(r'vitals', VitalViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
