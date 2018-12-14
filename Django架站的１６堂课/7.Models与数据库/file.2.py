# 　７．２　　活用Model制作网站

# ７．２．１　　建立网站

# 　django-admin.py startproject ch07www
#  mkdir templates
#  mkdir static
#  cd ch07www
#  python manage.py startapp mysite

# 然后，在settings.py的INSTALLED_APPS中加入'mysite',以及在TEMPLATES中设置DIRS为os.path.join(BASE_DIR,'templates'),
# 再与STATICFILES_DIRS中加入以下内容

# 以上这些是建立Django的标准步骤，接着到urls.py中加上index的网址对应关系

# 到models.py文件中,把前面的设计的models.py填入进去,接着admins.py中挼计入以下内容

#　最后，在命令提示符(或终端程序)执行以下指令，进行数据库的更新以及迁移操作，第一次使用数据库也要创建admin网页要使用的supernuser(超级用户)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py  createsuperuser
# python manage.py  runserver

#  Product数据表使用外键链接到PModel,所以在管理页面中会把PModel目前所有已输入的内容作为一个下拉式菜单,让Product在增加数据时可以选用,而且只能
# 选择其中之一,用户不能自行创建,这样就可以避免发生在产生新产品的时候没有指定手机型号的问题

# 7.2.2  制作网站模板

# 单一的数据表内容查询在起那么已有,为了网页文明美观,使用Template来建立网页内容.在此我们把页首和页尾分开,分别命名为header.html和footer.html
# 另外也准备了一个用来作为基础的base.html,在base.html中加入Bootstrap网页框架,最后创建index.html.base.html的内容主要加入Bootstrap框架链接以及
# 导入header.html和footer.html


# 在base.html中预留了两个block,分别是title和content,所有继承自这个template的文件都要准备两个block以供整合之用.header.html主要是
# 提供本网站的每一个网页用的标题和菜单


# footer.html用来放置本网站的logo图标以及版权声明.当然,如果有实体商店,就可以在这里放置商店的地址和联络电话


# 然后就是index.html的内容了,在开始设计views.index的内容之前,先看看index.html的框架应该是怎样的

# 在index.html中,要先指定继承自base.html(使用{% extends "base.html "%}),然后按序准备title和content这两个block的内容

# 7.2.3  制作多数据表整合查询网页


# 本网页的重点在于block content中的内容,也就是要呈现哪些数据?假设要呈现的内容是products这个列表数据,并使用HTML的表格功能显示,就可以使用一个循环来解决

# 我们使用{% for p in products %}把products列表中的数据一个一个拿出来显示,就会发现Product类设计有nickname,pmodel,year以及price这几个字段,
# 有手机型号但是没有制造商的字段.因为手机型号使用外键关联到Maker,所以我们可以使用p.pmodel.maker.name去取得这个手机型号的制造商,如果要显示手机
# 制造商的品牌国家或地区,使用p,pmodel.maker.country就可以了

# 使用跨表格查询的功能,在views.index中的数据库查询指令有没有特别的地方,django会自动会处理好


# 和之前的查询方式一样,products = models.Product.objects.all().不需要任何特别的处理,只要数据表之间的关系设置好,就和查询同一个数据表的方法一样
# 接下来要加入浏览每一个产品细节的功能,我们使用网址/detail/{id}来作为浏览产品详细内容的参数,先在urls.py加入一个网址样式,并命名为"detail-url"

# "(\d+)"可以识别在detail/之后的任意位数的数字.在index.html中列出所有手机之后,要在原本显示库存手机的字段内容加上链接,使用"detail-url"
# 在此使用product的id作为存取手段细节数据的索引值,因为它是默认的Primary Key,是唯一的值,所以用来作为搜索值自然是没有问题的

# 在detail中使用传进来的id进行搜索,使用models.Product.objects.get(id=id)来找出指定id的手机产品.注意,在django的ORM中如果使用get找不到
# 就会产生一个DoesNotExist的例外中断程序,为了避免程序被中断,在此使用try/execpt机制,让它发生except时直接pass,反正到时候product中会因为例外而没有内容
# 在detail.html中自然会有判断的机制

# 除此之外,找到product后,还要通过product去PPhoto中找到该产品在照片数据库中有没有存储内容,由于照片可能会超过1章张,因此使用filter来过滤,而
# 过滤用的参数直接使用刚刚找到的product就可以了.此函数的程序被中断,在此使用


# 7.2.4  调整admin管理网页的外观

# 在admin.py中,原本我们使用一般指令来设置要管理的Model类

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel','nickname','price','year')

admin.site.register(models.Product,ProductAdmin)

# 先从admin.ModelAdmin类中继承一个ProductAdmin子类,然后在admin.site.register时间时注注明要注册Model和要和使用的类,在子类中通过父类
# 提供的属性重新复写其设置,得到的结果.接着,如果想要增加自定 排序的功能以及搜索的功能,所以进一步修改admin.py


# 在此指定了要搜索的对象字段nickname,一开始显示的时候是以price为递减的方式来排序.其实,本来在admin管理页面中就有字段的功能,只要在字段名的
# 地方用鼠标点击就可以进行递增或递减的排序,使用ordering只是让显示数据一开始就把数据按照我们的需求排好

# 林伟,如果要把列表的标题字段名改为中文,可以在models.py定义字段加上verbose_name,在管理页面中就会主动采用了.同样以Product类为例,回到models.py去