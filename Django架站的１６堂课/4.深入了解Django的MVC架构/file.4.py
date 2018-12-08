# 4.4  Template简介

#  要建立专业网站,一定要使用高级功能的模板网页显示方法才行.也就是把HTML文件另外存成模板文件,然后把想要显示在网页的数据另外以变量的方式传送给渲染器,让
# 渲染器根据变量的内容和指定的模板文件进行整合,再把结果输出给网页服务器,本节就来使用Template建立专业的网站


# 4.4.1  创建template文件夹与文件


# Template模板渲染(即网页显示)有许多不同的引擎,但是Django有其默认值,一般情况下我们使用默认值即可.在使用之前,要先在网页中创建防止样板文件的文件夹,并在
# settings.py中设置此文件夹的存取地址.
# 首先,在当前的项目目录下创建一个名为templates的文件夹,它的等级和manage.py,db.sqlite3是同一层.接着到settings.py中找到TEMPLATES的设置,
# 把DIRS中原本空下来的[]内容填入当前所在的位置os.path.join(BASE_DIR,'templates')

# 接着,在templates文件夹中创建一个about.html文件  hr标签会创建一条水平线

# 这是about函数中html变量的内容,但是在后面我们加了一个"今日佳句"的功能更,把quote变量放在"{{}}"中,即可在网页打开时显示出来

# 4.4.2  传送变量到template文件中
# 要使用Template网页显示功能,在views.py的最前面使用import get_template 模块.我们在about函数中也用到了随机数的功能,所以views.py的import
# 内容如下:
#  在程序中,首先使用get_template函数取得about.html文件的执行实例,然后用template.render()方法函数执行网页显示的工作.而render函数需要使用什么变量?
# 要以json类型传送进去.在此例中,我们要显示quote变量,因此会在render函数中传送"{'quote'":random.choice(quotes)}"参数进去,如此在about.html
# 中就可以顺利取得quote变量,并把它显示出来.渲染后的网页数据被放进html变量中,再使用HttpResponse函数把它传给网页服务器即可

#  同样的方法也可以使用到disp_detail函数中, 注意,render在渲染时会把变量中的内容当做一般的字符来处理,而不是HTML标记,其实在这个例子中,不该在views.py
# 中处理网页呈现的问题,应该回归到template文件中才对.因此,我们要做的是把变量传到disp.html中,然后在disp.html中以Templated的命令来处理
# 新版本的disp_detail函数编码.确实把存取数据的逻辑和设计显示网页内容的部分完全分割开,程序变得更加简洁

#　4.4.3  在template中处理列表变量

# 那么在listing函数中要显示全部数据项列表，又要如何编写
#  继续前面的思维，程序变得非常简单，把找到的products列表变量直接放到template中就可以了，真正显示内容的格式
# 则放在list.html
# 因为products是一个列表变量，因此在真正显示出内容之前，可以使用templatede循环指令{% for %}/{% endfor %}，其中{%%}符号是用来下达template指令的地方
# 常用的有for语句和if语句.要注意的是endfor中间没有空格.使用{% for p in products %}基本上和Python处理for循环是一样的,它会逐一把
# products列表中的每一个元素取出来放在p中,接着就可以在适当的html标记中插入{{}}显示变量内容的标记.


