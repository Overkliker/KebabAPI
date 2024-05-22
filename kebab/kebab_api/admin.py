from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Roles)
admin.site.register(Users)
admin.site.register(OrderFeedbacks)
admin.site.register(KebabIngredients)
admin.site.register(Kebabs)
admin.site.register(KebabsOrdered)
admin.site.register(Workers)
admin.site.register(Points)
admin.site.register(Profiles)
admin.site.register(Ingredients)
admin.site.register(FromOrder)
admin.site.register(Orders)