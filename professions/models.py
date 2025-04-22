from django.db import models

class Profession(models.Model):
    profession_name = models.CharField(max_length=100, unique=True)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    future_salaries = models.JSONField(default=list)
    companies = models.JSONField(default=list)
    experience = models.CharField(max_length=3, default="JR")

    def __str__(self):
        return self.profession_name