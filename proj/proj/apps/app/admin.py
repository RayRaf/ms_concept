from django.contrib import admin
from .models import  Product, Project, Supplier, PositionalTag, DocSection, Property_name, Property_value

# Register your models here.

admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Supplier)
admin.site.register(PositionalTag)
admin.site.register(DocSection)
admin.site.register(Property_value)
admin.site.register(Property_name)


