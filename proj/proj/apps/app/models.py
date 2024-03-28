from django.db import models

# Create your models here.


class Project(models.Model):
    project_code = models.CharField('Шифр проекта', max_length = 200)
    project_description = models.CharField('Описание проекта', max_length = 400)

    def __str__(self) -> str:
        return self.project_code
    

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'



class Product(models.Model):
    product_name = models.CharField('Название изделия', max_length = 200)
    product_order_code = models.CharField('Артикул изделия', max_length = 200)
    product_price = models.FloatField('Цена изделия')
    product_price_currency = models.CharField('Валюта цены', max_length = 3)
    supplier = models.ForeignKey('Supplier', on_delete = models.SET_NULL, null = True)


    def __str__(self) -> str:
        return self.product_name + ' ' + self.product_order_code

    class Meta:
        verbose_name = 'Комплектующее изделие'
        verbose_name_plural = 'Комплектующее изделие'

    
class Supplier(models.Model):
    supplier_name = models.CharField('Название фирмы поставщика', max_length = 100)
    supplier_email = models.CharField('Почта поставщика', max_length = 50)

    def __str__(self) -> str:
        return self.supplier_name
    
    class Meta:
        verbose_name = 'Поставщик'        
        verbose_name_plural = 'Поставщики'


class PositionalTag(models.Model):
    tag = models.CharField('Позицоинное обозначение', max_length = 50)
    project = models.ForeignKey(Project, on_delete = models.SET_NULL, null = True)
    product = models.OneToOneField(Product, on_delete = models.SET_NULL, null = True)
    docsection = models.ForeignKey('DocSection', on_delete = models.SET_NULL, null = True)
    def __str__(self) -> str:
        return self.tag

    class Meta:
        verbose_name = 'Поз. обозначение'        
        verbose_name_plural = 'Поз. обозначения'

class DocSection(models.Model):
    section_name = models.CharField('Полное название раздела', max_length = 100)
    code_name = models.CharField('Кодовое обозначение раздела', max_length = 10)

    def __str__(self) -> str:
        return self.code_name

    class Meta:
        verbose_name = 'Раздел документации'        
        verbose_name_plural = 'Разделы документации'