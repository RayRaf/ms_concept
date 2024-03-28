from django.contrib import admin
from .models import  Product, Project, Supplier, PositionalTag, DocSection

# Register your models here.

admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Supplier)
admin.site.register(PositionalTag)
admin.site.register(DocSection)

