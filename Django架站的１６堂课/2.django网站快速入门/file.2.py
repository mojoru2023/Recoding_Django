# 2.2  创建博客数据表

#  2.2.1  数据库与django的关系

#  在默认的情况下，django的数据库以model的方式来操作，在程序中不直接面对数据库以及数据表，而是以class类先创建好model,然后通过对
#  model的操作达到操作数据库的目的．这样的好处是把程序和数据库之间的关系以中介层作为连接的接口，日后如果需要更换数据库系统的话，可以不更改程序的部分

#  在django中使用数据库，有以下几个步骤


#  步骤１．　　在models.py中定义需要使用的类(继承自models.Model)
#  步骤２　详细地设置每一个在类中的变量，即数据库中的每一个字段
#  步骤３　使用python manage.py makemigrations mainsite　创建数据库和django建的中介文件
#  步骤４　使用 python manage.py migrate同步更新数据库的内容
#  步骤５　在程序中使用python的方法操作所定义的数据类，等于在操作数据库中的数据表


#  ２．２．２　　定义数据模型

#　mblog需要一个用来存储文章的数据表，因此需要修改mainsite/models.py的内容，
# 在这个文件中，主要是创建一个Post类(到时候在数据库中会有一个对应的数据表)，此类包括几个项目，title来显示文章的标题，slug是文章的网址
# body是文章的内容，pub_date是本文发表的时间．class Meta 内的设置则要指定文章显示的顺序是以pub_date为依据，最后__unicode__提供此类
# 所产生的数据项－－－一个以文章标题作为显示的内容，增加操作过程中的可读性(在管理界面或shell界面操作时)，使用unicode而不是str,
# 让这个这个标题可以正确地支持中文标题

#pub_date,我们以timezone.now的方式让它自动产生，还需要一个pytz模块，　安装　pip install pytz


# 要让此模型生效，需要执行以下指令：
# 　　python manage.py makemigrations mainsite
#  python manage.py migrate

# 此时就可以在程序中直接操作此数据库了.启动django提供的admin界面来操作会更加方便

# 2.2.3  启动admin管理界面
# admin是django默认的数据库内容管理界面,在使用前,有几个要设置的步骤,第一个创建管理员账号即密码

#   python manage.py createsuperuser

#　修改mainsite/admin.py 　也就是先导入Post类，然后通过admin.site.register注册．完成以上设置后，在此打开网站，通过浏览器
#  为了标语后续测试,至少要输入5篇文章,中英即可但是slug要使用英文或数字,而且中间不要使用任何符合和空格符

# 最后,在admin.py章加入以下程序代码(自定义Post显示方式的类,继承自admin.ModelAdmin),让文章在显示的时候除了title外,还要加上张贴的时间和日期内容

# 2.2.4 读取数据库中的内容


# 数据库中有了文章后,就要读取这些资料,然后在网站的首页中把它们显示出来.在此先简单说明一下django的MTV(大约可以模拟到MVC)架构.为了把数据
#  抽象化,django把数据的存取和显示区分为Model,Template以及View,分别对应models.py,template文件夹以及views.py这些文件

#  models.py主要负责定义要存取的数据模型,以Python的class类来定义,在后端django会自动把这个类中的设置对应到数据库系统中,
#  在View中,也就是在views.py中处理,这也是本节要编写的地方.至于如何把取得的数据用美观且有弹性的方式输出,在Template中处理

#  第一步把在
