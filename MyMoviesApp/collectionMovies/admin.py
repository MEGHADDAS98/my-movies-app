from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.



from collectionMovies.models import Collection,CollectionMovie,RequestCounter,Movie


admin.site.register(Collection)
admin.site.register(CollectionMovie)
admin.site.register(RequestCounter)
admin.site.register(Movie)
# admin.site.register(Basket)
# admin.site.register(LineItem)
# admin.site.register(OrderItem)
# admin.site.register(BasketItem)