from django.contrib import admin
from .models import User, Auction, Bid, Comment

# Register your models here.
class AuctionsAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "user", "category", "price")
class BidAdmin(admin.ModelAdmin):
    list_display = ("amount", "bidder", "listing")
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "listing")

admin.site.register(User)
admin.site.register(Auction, AuctionsAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)