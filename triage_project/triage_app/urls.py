from django.urls import path, include
from rest_framework import routers
from .views import (PatientViewSet, VisitFormViewSet,
                    VitalViewSet, PatientViewSetBrief,)

router = routers.DefaultRouter()


router.register(r'patients-brief', PatientViewSetBrief, basename='patients-brief')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'visit-forms', VisitFormViewSet)
router.register(r'vitals', VitalViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
