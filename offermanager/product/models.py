from django.db import models
from django_countries.fields import CountryField


class Bank(models.Model):
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.name}, {self.account_number}'


class Location(models.Model):
    country = CountryField(default=None, blank=True, null=True)
    city = models.CharField(default=None, max_length=200, blank=True, null=True)
    street = models.CharField(default=None, max_length=200, blank=True, null=True)
    houseNum = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.houseNum}'


class Waybill(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    finish_date = models.DateField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    document_serias = models.CharField(max_length=5, default="MP")
    document_number = models.PositiveIntegerField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.customer_name}, {self.created_at}"

    class Meta:
        ordering = ("price", "created_at",)


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    code = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.code}"
