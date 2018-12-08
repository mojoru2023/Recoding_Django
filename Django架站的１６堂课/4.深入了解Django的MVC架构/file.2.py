# 4.2  Model简介

# Model是Django表示数据的格式,以Python的类为基础在models.py中设置数据项与数据格式,基本上每个类对应一个数据库中的数据表.因此
# 定义每个数据项时,除了数据项名外,也要定义项目的格式以及这张表格和其他表格相互之间的关系(即数据关联)
# 定义完毕之后.网站的其他程序就可以使用Python语句来操作这些数据内容.

# 4.2.1  在models.py中创建数据表

# 刚创建的网站项目,models.py只有一行内容
from django.db import models

#　此行语句导入了models作为创建数据类的基类．在参数中别忘了导入model.Model,然后就可以使用models.*来指定数据表中每一个字段的特征．

# 每一个字段还有一些共享的选项可以设置，这些选项的设置和数据库的设置息息相关，常用的设置选项摘要如下

# 别忘了在settings.py的INSTALLED_APP设置中要有这个App的名称,首次设置Model的内容要先执行makemigration的指令以及migration指令

# python manage.py makemigrations

# python manage.py migrate

# 然后系统就会把我们设置的NewTable数据表建立到数据库中，哪种数据库，要在setttngs.py的数据库中设置，默认是sqlite.也就是存在于同一个文件夹下的db.sqlite3wenjian
# 这个数据表是使用了哪些设置所创建出来的呢?先观察在 mysite/migrations文件夹下的文件,会看到0001_initial.py以及 __init__.py这两个文件,
# 其中0001_initial.py文件就是记录第一次Model设置的数据表内容,因为一开始只有一个设置,所以只有00001这个版本好,我们可以使用
# sqlmigrate指令显式出我们所设置的NewTable类转换成sql语句的样子
# python manage.py sqlmigrate myapp  0001

# django默认加上了一个id字段,设置为主键,并自动增加了数值内容,以便它内部的数据管理

# 4.2.2 在admin.py中创建数据表管理界面

# 在models.py中创建类之后,只要接着admin.py中加入这个NewTable,就可以在/admin中管理这张数据表了
# (第一次使用时要先使用createsuperuser创建一个在/admin中的管理员账号即密码),admin.py的内容
#     python manage.py createsuperuser
# 此时通过    python manage.py runserver  启动测试网页服务器,然后打开浏览器连接 http://localhost:8000/admin

# 网站的数据库经常会反应网页上的输入窗体的使用情况,而输入窗体中常常会有一些字段提供候选数据(例如在窗体中询问喜欢的颜色,品牌车型,尺寸大小等)
# 供网友选择,我知道要使用choices选项,那么应该如何使用?我们以创建一个产品类为例,在models.py中加入如下内容
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)


# 先创建一个名为SIZES的元组,其中每一个元素也是元组,第一个项目是要被实际存储的内容,此例为"S","M","L",后面那个项目是对应的说明,此例为"Medium","Large","Small"
# 编辑models.py,一定要再执行migrate才行(如果中间修改过,就需要先执行makemigration),这两个指令简单地看就是要求套用最新的数据表的新增或修改的内容



# python manage.py makemigrations
# python manage.py migrate

# 进入Product的操作界面,在选择添加记录后,可以看到Add product页面中,Size 采用列表的方式呈现

#　也可以修改类的属性名，主要在models.py中更改即可．但是要注意的是，因为Django把数据库的操作抽象化了，每一个新增以及修正步骤都必须被记录，
# 以便后续的数据库迁移操作，所以除了在models.py中把修改一下属性名之外，要在执行以下下面两步
# (还会需要改进)把实例名称改过来


# python manage.py makemigrations
# python manage.py migrate

# 4.2.3   在python Shell 中操作数据表

#  前面学习到了如何在程序中存取数据库中的数据,基本上在python程序中不适用sql指令来存取数据,而是以ORM的方式来存取数据库里的内容.ORM
# 是一种面向对象的程序设计技术,以对象的方式来看待每一笔数据,可以解决底层数据库兼容性的你问题,也就是把数据库的操作方式抽象化为统一在python中习惯
# 的数据操作方式,如果把这些张丽玲对应到实际每一种数据库的内部操作,就由元数据以及Django内部去处理,开发人员不用担心这个部分
#　在前面定义的数据表，可以在python的交互式界面中直接进行存取操作

# 　python manage.py shell

# python manage.py shell 是进入拥有此网站环境的python shell ,一开始当然要使用  from myapp.models import NewTable,Post,Produ
# 来导入在models.py中建立的Product数据表．接下来，通过Product.objects.create指令创建一组记录，同时别忘了把这组创建好的数据记录交给任意一个
# 变量(此例子为p)持有，然后通过p.save()把它真正存储到数据表中．在离开后，回到/admin界面中，即可查询此记录
# 当然在shell　中也可以显示记录的内容，只要使用Product.objects.all()函数就可以获取的所有的数据，其数据类型称为QuerySet,类型

#   Python manage.py shell
#  from myapp.models import NewTable,Post,Produ
#  allp = Produ.objects.all()

#  把取得的所有记录放在allp中，因为目前只有一项数据，所以只要使用allp[0]就可以取得这笔数据，就像是简单的列表操作一样．然而，在这里显式出来的数据内容是
# <Produ: Produ object> 在Product类中可以使用同样的方法,也就是在class Product中加入如下函数

def __unicode__(self):
    return self.name

#　这个函数是在这个类的实例被打印出来的时候会调用的函数，我们直接把它复写成显示其中的name字段，此例中会把产品的名称打印出来，如此就可以清楚
#　地了解数据记录的内容了


#　４．２．４　　　数据的查询与编辑

#　Django的ORM操作是最重要的是找到数据项(记录)，把它放到某一个变量中，然后就可以针对这个变量做任何想要的操作，包括修改其中的内容，只要
#　最后调用了save()函数，修改的内容就会反映到数据库中

#　除了之前的create(),save()和all()三个函数外，其他常用的函数以及可以加在函数中的修饰辞摘要
#　Ｄjango ORM常用的函数以及修饰词

#　有一些函数(如reverse(),exists()等)可以串接在另一些函数后面，用于进一步过滤信息，修饰词则放在参数中，在字段名后面加上２个下划线之后再串接，
#　可以为条filter只能设置等号，如果要使用小于２的条件，修改如下

#　　less_than_two =  Produ.objects.filter(qty_lt=2)

#  在练习之前,别忘了在/admin管理页面多输入几笔数据到数据库中,方便看出各个函数和修饰词的实际用途.现在假设我吗要建立一个中古手机的管理页面,
# 已在数据库中建立了5个数据想,另外在Produ类中多加了一个qty字段,用来记录目前的库存数据了,

# 这里用到给数据模型增加新字段的操作
# 1. 先在models.py中模型类中增加字段名,如这里是  qty = models.IntegerField(blank=True,null=True)
# 2. 在命令行中打开, 执行 python manage.py  makemigrationas myapp(应用名称)
# 3. 输入1 (这里要求你设置新字段的默认值,他会在新建这个字段的同时把默认值也添加上去)
# 4. 如果不想让它有值,我们直接输"(中间没有空格),一样可以达到效果,但是不能不设置默认值,(如果是数值类型,默认值为"不行,如果是年龄,
# 需要设置blank=True和null=True)

# (blank:设置为True时,字段可以为空.设置为Flase时,字段是必须填写的,字符型字段CharField和TextField是用空字符串来存储空值的,
# 如果为True,字段允许为空,默认不允许)
# null:　设置为True时，djang用Null来存储空值．日期型，时间型和数字型字段不接受空字符串．所以设置IntegerField，DateTimeField型
# 字段可以为空时，需要讲blank,null设为Ｔrue.如果为True,空值将会被存储为null,默认为False．如果想设置BooleanField为空时
# 可以选择NullBooleanField型字段）

# ５．　最后输入：  python manage.py migrate

# 　查看数据库，新字段已经加进去了，如果你设置了默认值，原来的这些数据的值都会设为你设置的默认值

# Produ.objects.all()

#  同样都是查询数据，使用filter会返回一个列表，而使用get会返回一个唯一的值．如果在设置的条件下找不到任何数据，使用filter就会返回一个空列表，
fr# 　而使用get会产生一个DoesNotExist例外，如果设置的条件有一个以上的元素符合条件，那么set也会产生例外．因此，get通常在明确知道该数据只有一笔
# 的情况下才会使用，而且使用的时候也要以try/exception　做好例外处理工作，正因为如此，大部分情况下，笔者都是使用filter来搜索数据


