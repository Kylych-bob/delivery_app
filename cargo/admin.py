from django.contrib import admin

from cargo.models import Weight, Price, Distance


class DistanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'latitude_2', 'latitude_1', 'longitude_2', 'longitude_1')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    # list_editable = ('',)
    # list_filter = ('')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class WeightAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)



admin.site.register(Distance, DistanceAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Weight, WeightAdmin)








#   longitude_1
#     longitude_2
#     latitude_1    
#     latitude_2