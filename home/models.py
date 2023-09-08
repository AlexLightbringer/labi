from django.db import models

class Job(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100, blank=False)
    phone = models.CharField(verbose_name="Phone", max_length=10, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=50, blank=False)
    text = models.TextField(verbose_name="Comment", max_length=300, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"