from django.db import models
import uuid


class Job(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100, blank=False)
    phone = models.CharField(verbose_name="Phone", max_length=10, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=50, blank=False)
    text = models.TextField(verbose_name="Comment", max_length=300, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"


def file_upload_path(instance, filename):
    return f"order_files/{filename}"


class Order(models.Model):
    client = models.CharField(verbose_name="Client", max_length=100, blank=False)
    phone = models.CharField(verbose_name="Phone", max_length=10, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=50, blank=False)
    order = models.TextField(verbose_name="Order comment", max_length=300, blank=False)
    order_number = models.CharField(
        verbose_name="Order Number", max_length=20, unique=True, blank=False
    )
    file_upload = models.FileField(
        verbose_name="File Upload", upload_to="order_files/", blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.client}"

    def generate_order_number(self):
        return str(uuid.uuid4().hex[:10])

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)
