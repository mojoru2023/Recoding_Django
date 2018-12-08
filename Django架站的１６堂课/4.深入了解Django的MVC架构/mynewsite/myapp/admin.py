from django.contrib import admin


# Register your models here.

from .models import NewTable,Post,Produ # 同一个文件夹下导入相邻的模块,把设计的数据模型在此注册



admin.site.register(NewTable)
admin.site.register(Post)
admin.site.register(Produ)