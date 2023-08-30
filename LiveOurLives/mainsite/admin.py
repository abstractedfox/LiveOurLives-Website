from django.contrib import admin
from mainsite.models import MinimizerRetorts, InfoCategories, ActualInformation

# Register your models here.
class MinimizerRetortsAdmin(admin.ModelAdmin):
    pass
    
class InfoCategoriesAdmin(admin.ModelAdmin):
    pass
    
class ActualInformationAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(MinimizerRetorts, MinimizerRetortsAdmin)
admin.site.register(InfoCategories, InfoCategoriesAdmin)
admin.site.register(ActualInformation, ActualInformationAdmin)
