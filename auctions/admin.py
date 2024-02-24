from django.contrib import admin

from .models import User, Auction, Comment, Bid, Watchlist
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)