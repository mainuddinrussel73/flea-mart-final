from django.contrib import admin

# Register your models here.

from User.models import SellItemInfo,Chat,Notification,Comments,ServerInfo,Auctions

# Register your models here.


admin.site.register(ServerInfo)
admin.site.register(SellItemInfo)
admin.site.register(Chat)
admin.site.register(Notification)
admin.site.register(Comments)
admin.site.register(Auctions)
admin.site.site_header= 'Online Flea Mart'
