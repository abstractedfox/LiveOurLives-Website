from django.contrib import admin
from mainsite.models import MinimizerRetorts, InfoCategories, ActualInformation, ImageInfo, MultiExcerpt

# Register your models here.
class MinimizerRetortsAdmin(admin.ModelAdmin):
    pass
    
class InfoCategoriesAdmin(admin.ModelAdmin):
    pass
    
class ActualInformationAdmin(admin.ModelAdmin):
    pass

class MultiExcerptAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(MinimizerRetorts, MinimizerRetortsAdmin)
admin.site.register(InfoCategories, InfoCategoriesAdmin)
admin.site.register(ActualInformation, ActualInformationAdmin)
admin.site.register(ImageInfo)
admin.site.register(MultiExcerpt, MultiExcerptAdmin)
