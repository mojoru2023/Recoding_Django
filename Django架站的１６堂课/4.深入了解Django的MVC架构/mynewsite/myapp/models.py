from time import timezone

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title


class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20,unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()
    def __unicode__(self):
        return self.bigint_f

class Produ(models.Model):
    SIZES = (
        ('S','Small~~~~'),
        ('M','Medium'),
        ('L','Large'),
    )
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1,choices=SIZES)
    qty = models.CharField(max_length=20)

    # def __unicode__(self):  # 这个形式python3不再用了
    #     return self.name
    #
    def __Unicode__(self): # 打印输出实例
        return self.name, self.sku, self.price, self.size, self.qty

    def __str__(self): # 在网页上显示出来
        return self.name, self.sku, self.price, self.size, self.qty





