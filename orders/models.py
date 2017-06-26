from django.db import models
from django.contrib.auth.models import User


class Technology(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False, default='---')
    image = models.ImageField(upload_to='images/tech_images/')
    mini_image = models.ImageField(upload_to='images/tech_images/')


class Currency(models.Model):
    complete_name = models.CharField(max_length=3, blank=False, null=False, default='USD')
    short_name = models.CharField(max_length=2, blank=False, null=False, default='$')


class PaymentType(models.Model):
    payment_type = models.CharField(max_length=10, blank=False, null=False)


class PaymentTypeInOrder(models.Model):
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    min_payment = models.IntegerField(blank=False, null=False, default=0)
    max_payment = models.IntegerField(blank=False, null=False, default=0)


class Order(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bidders = models.ManyToManyField(User)
    required_technologies = models.ManyToManyField(Technology)
    bids_count = models.IntegerField(blank=False, null=False, default=0)
    average_bid = models.IntegerField(blank=False, null=False, default=0)

