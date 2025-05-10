from django.db import models


# Create your models here.
class Donor(models.Model):
    blood_group = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    when_needed = models.DateTimeField()
    contact_number = models.CharField(max_length=11)
    description = models.CharField(max_length=300)
    disease_description = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Condition Requiring Blood"
    )

    def _str_(self):
        return self.blood_group