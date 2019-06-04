from django.db import models


class Pitches(models.Model):
    ba = models.IntegerField(blank=True, null=True)
    sku_code = models.IntegerField(blank=False, unique=True, null=False) # getting only unique fields
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField()
    ean = models.FloatField(null=True, blank=True)
    manufacturer = models.CharField(max_length=255)
    brand = models.CharField(blank=False, null=True, max_length=255)
    flavor = models.CharField(max_length=255)
    package = models.CharField(blank=False, null=True, max_length=255)
    size = models.CharField(max_length=255)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    depth = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'pitches'            # Displays after clicking name field
        verbose_name_plural = 'pitches'     # Display in Admin get name list

    def __str__(self):
        return self.name

