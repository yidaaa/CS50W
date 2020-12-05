from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    def __str__(self):
        return self.username

class Auction(models.Model):
    CATEGORY = [
        ('clothes', 'Clothes'),
        ('shoes', 'Shoes'),
        ('electronics', 'Electronics'),
        ('food', 'Food'),
        ('displays', 'Displays'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('furniture', 'Furniture'), 
        ('miscellaneous', 'Miscellaneous'),
    ]
    title = models.CharField(max_length= 50)
    description = models.TextField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    category = models.CharField(max_length = 40 , choices= CATEGORY , default="None")
    image_url = models.URLField(default="" , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="owner")

    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    watching = models.ManyToManyField(User, blank=True, related_name="users_watching")
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="bidder")

    def __str__(self):
        return self.title

class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing = models.ManyToManyField(Auction, blank=True, related_name="items_watched")

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)

    