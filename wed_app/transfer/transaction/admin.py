from django.contrib import admin
from .models import Chek, Type, Status, Category, SubCategory
from .forms import ChekForm

admin.site.register(Chek)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(SubCategory)


class ChekAdmin(admin.ModelAdmin):
    form = ChekForm
