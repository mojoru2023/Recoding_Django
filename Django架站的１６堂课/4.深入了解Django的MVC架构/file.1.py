# 第4章 深入了解Django的 MVC框架

# M:模型, V:视图,   C:控制

#  4.1 Django的MVCJIAKGOUJIANJIE

# Model数据模块
# 包含系统中的数据内容,通常以数据库的形式来存储,如果这些内容有变动,就会通知view实时更改显式的呢日用,一些处理数据的程序逻辑也会放在这里
# View视图模块
# 创建和用户之间的界面,把用户的请求传送给Controller,并按照Controller的要求把来自Model的数据显式出来
# Controller控制模块
# 派发view传来的用户请求,并按照这些请求处理数据内容以及设置要显示的数据
# 在一个大型项目中,团队协作,例如负责数据库的人员,外观设计的人员以及程序编写人员在协作

# 4.12  Django的MTV架构

# 网页服务器本身在派发工作的时候就隐含了控制的逻辑,网页框架中Template模板文件的套用又是最常用被使用的网页显示技巧,所以Django主要的架构形成
# 了使用Model,Template和View三部分的搭配,分别对应网站的数据存储model.py,网站的模板文件组(一般是放在templates文件夹下的html文件)
# 以及控制如何处理数据程序逻辑的view.py.其中很多控制逻辑被放在整个Django Framework中(如,urls.py的设置
#用户浏览器,到网页服务器apache,再到urls.py派发网址,再到views.py视图,再到models.py模型,对接数据库,
#　返回从views.py视图，再到网页模板Templates，再到网页服务器apache


# 使用templates来做每个网页的外观框架，送至templates中要被使用的数据尽量是直接显示的简单形式，不要视图在template文件中使用复杂的方法处理
# 这些送进来的变量，如果需要对变量进行更复杂的运算，那么这些工作应该放在views.py中完成．即便是一个人独立操作的网站，也要想象template是由不太熟悉
# 程序设计的网页美工人员负责的
# 在models.py中定义所有需要用到的数据格式，一般是一数据库的形式存储的，定义后的Ｍodel数据库类要把它import到views.py中，主要的操作流程为：
# 用户在浏览器下达request.这个request会先被送到网站服务器中做分派的工作，这个分派指定在urls.py中完成．每一个分派的工作都会被设置成views.py
# 中的函数，也就是主要处理数据的逻辑，在views.py中完成．因此，所有在urls.py指派的函数要在urls.py的前面import才行

# 4.13  Django网站的构成以及配合
#  django-admin startproject mynewsite
# 然后通过python  manage.py startapp myapp指令,
# 整个项目的名称是mynewsite,和此项目同名的mynewsite/mynewsite 文件夹放置的是属于全站的设置,myapp是此网站中额一个app,只要好好设计,日后就可以
# 重复使用(Reuse,重用)在不同网站中的可携带模块.因此,settings.py,urls.py以及wsgi.py都属于全站的设置
# models.py,views.py,tests.py以及admin.py则是跟着可重用模块跑的内容
# 初学者要把myapp文件夹的内容看做以models.py为中心,先设计要操作的数据,然后在views.py中设计操作(存取)这些数据的方法,而admin.py是附赠
# 的通用型数据管理界面

# 最后,由于此项目网站的根目录是mynewsite,因此创建模板和放置静态文件的目录放在此文件阿基即可

#　４．１．４　　在Django　MTV架构下的网站开发步骤
# 要开发Django MTV架构的网站,如果是大型项目,标准的需求分析,系统分析与设计以及各种各样的软件工程步骤就一项不能少,以增加日后此项目的可维护性,降低
# 未来修改错误所产生的成本.对于初学者,要做的只是小小的练习项目,


# 步骤1, 需求分析不可少,一定要具体列出本次网站项目所要实现的目标,可能包括简单的页面草图与功能方块图等

# 步骤2, 数据库设计,   在需要分析后,开始创建数据模块前,网站中所有会用到的数据内容,格式以及各个数据之间的关系一定要理清,最好事先把要创建的数据表确定清楚,减少
# 开始设计程序后修改Model的工作,例如要创建留言板程序,就要知道每一则留言要记录的项目有哪些,接不接受响应消息,要不要记录被浏览的次数,有没有提供逼着登录等
# 很典型的情况是,如果每则留言都可接受响应,那么存储响应的数据表和留言本身的数据表机会有数据表关联的设置,这是不可少的

# 步骤3  了解网站的每一个页面,并设计网页模板(.html)文件
# 步骤4  使用virtualenv创建并启用虚拟机环境
# 步骤5 使用pip install 安装django(本书以django1.8为主),
# 步骤6 使用django-admin startproject生成项目
# 步骤7 使用python manage.py startapp创建app
# 步骤８　创建templates文件夹，并把所有网页模板(.html)文件都放在此文件夹中
# 步骤9创建static文件夹,并把所有静态文件(图片文件,.css文件以及.js)都放在此文件夹中
# 步骤10 修改settings.py,把相关文件夹设置都加入,也罢生成的app名称加入INSTALLED_APPS序列中
# 步骤11 编辑 models.py,创建数据库表格
# 步骤12 编辑views.py,先import在models.py中创建的数据模型
# 步骤13 编辑admin.py,先把models.py中定义的数据模型加入,并使用admin.site.register注册新增的类,让admin界面可以处理数据库内容
# 步骤14 编辑views.py,设计处理数据的相关模块,输入和输出都通过templates相关的模块操作获取来自与网页的输入数据,以及显示.html文件的网页内容
# 步骤15 编辑urls.py.先import在views.py中定义的模块
# 步骤16 编辑urls.py创建网址和views.py中定义的模块的对应关系
# 步骤17 执行 python manage.py makemigrations
# 步骤18 执行 python manage.py migrate
# 步骤19 执行 Python manage.py runserver ceshi 测试网站

#　以上的步骤反反复复，使用到在别的文件中定义的类或模块，要先导入


