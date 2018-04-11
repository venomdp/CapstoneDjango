from django.db import models

class vuln(models.Model):
    CVE = models.CharField(max_length=30)
    dateStart = models.DecimalField(max_digits=30, decimal_places=0)  # For epoch time #
    dateEnd = models.DecimalField(max_digits=30, decimal_places=0)  # For epoch time #
    score = models.DecimalField(max_digits=4, decimal_places=2)  # Can edit as needed, assumed scores could have decimals #
    link = models.CharField(max_length=100)




