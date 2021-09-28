from django.db import models

GENDER = (
    ('M', "MALE"),
    ('F', "FEMALE"),
    ('N', "NO_SAY"),
)

HEALTH = (
    ('G', "GOOD"),
    ('B', "BAD"),
)

DIET_HISTORY = (
    ('Y', "YES"),
    ('N', "NO"),
)


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=1, choices=GENDER,)

    class Meta:
        pass

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Vital(models.Model):
    height = models.DecimalField(max_digits=10, decimal_places=5)
    weight = models.DecimalField(max_digits=10, decimal_places=5)
    bmi = models.DecimalField(max_digits=10, decimal_places=5)
    patient_fk = models.ForeignKey(
        Patient, models.CASCADE, related_name='vitals')

    class Meta:
        pass

    def __str__(self):
        return str(self.id)


class VisitForm(models.Model):

    health_status = models.CharField(
        max_length=1, choices=HEALTH,)
    on_diet = models.CharField(
        max_length=1, choices=DIET_HISTORY,)
    patient_fk = models.ForeignKey(
        Patient, models.CASCADE, related_name='visit_forms')
    comments = models.CharField(max_length=1000)

    class Meta:
        pass

    def __str__(self):
        return str(self.id)
