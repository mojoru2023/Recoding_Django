# 2.3 网址对应与页面输出

# 个人博客最重要的地方除了提供输入文章内容的编辑页面外,如何在网页中显示出文章内容也是重点
#  当网友来到网站首页的时候,会以链接的方式显示每篇文章的标题,用鼠标点击任一个链接,即可

#　２．３．１　　创建网页输出模板template


#　步骤１　　在settings.py 中设置模板文件夹的位置
#　步骤２　　在urls.py中创建网址和views.py中函数的对应关系
#　步骤３　　创建.html文件(如index.html)，做好排版并安排数据要放置的位置
#　步骤４　　运行程序，以objects.all()在views.html中取得数据或资料
#　步骤５　　以render函数把数据(如posts)送到指定模板

#　使用一个小技巧把变量放到模板中，就是使用locals()函数．这个函数会把当前内存中的所有局部变量使用字典类型打包起来，刚好可以在这里排上永昌
#　在模板中因为接收到了所有局部变量，所以也可以把posts和now都拿来使用

#　2.3.2 网址对应urls.py

#　步骤１　　在urls.py中设置，只要是/post/开头的网址，就把后面接着的文字当做参数传送slug给post_detail显示单篇文章的函数
#　步骤２　在views.py中新增一个post_detail函数，除了接收request参数外，也接收slug参数
#　步骤３　在templates文件夹中创建一个用来显示单篇文章的post.html
#　步骤４　在post＿detail函数中，以slug为关键词搜索数据集，找出是否又符合的项目
#　步骤５　如果有符合的，就把找到的数据项传送给render函数，找出post.html模板页进行渲染(即进行网页显示)，再把结果交给HttpResponse回传给浏览器
#　步骤６　如果没有如何的项目，就把网页转回首页

#  通过url(r'post/(\w+)$',showpost)的设置,把所有post/开头的网址后面的字符串都找出来,当做第2个参数(第1个参数是默认的request)_传送给showpost函数,
#  showpost在import的地方要记得导入,同时到views.py中新建这个函数来处理接收到的参数
#  考虑到可能会有自行输入错误网址以至于找不到文章的情况,除了在Post.objects.get(slug=slug)搜索文章是加上例外处理,也在发生例外的时候以
#  redirect('/')的方式直接返回首页,因此不要网络在前面导入redirect模块

# 在设计index.html和post.html 的时

#  2.3.3  共享模板的使用
# 把每一个网页共同的部分独立出来成为另一个文件才是最正确的做法.Django就提供了共同模板的方式处理这部分机制

#  base.html   网站的基础模板,提供的网站的主要设计,外观风格
#  header.html  网站中每一个网页共享的标题元素,通常是放置网站Logo的地方
#  footer.html  网站中每一个网页的共享页尾,用来放置版权声明或其他参考信息
#  index.html  此范例网站的首页
#  post.html  此范例网站用来显示单篇文章的网页


# 设计一个base.html的主要模板,在此base.html中导入header.html和footer.html,等于是让header.html和footer.html分开设计.
# 主要显示的文件index.html 和post.html,则用extends指令继承自base.html,以保持网页风格的一致性

#  一般的html文件加上{%...%}的模板指令.在这些模板指令中,如果没有意外,使用include'.html文件名'就可以导入指定的模板文件,此文件中分别在适当的地点导入
# header.html和footer.html.此外,通过block指令可以到后面加上此block(区块)的名称,也就是在index.html中填入内容的位置.在此base.html中
# 分别在适当的地点指定 title headmessage 和content.因为在base.html指定了3个区块,所以接下来继承base.html 的所有文件都要
# 提供这3个区块的内容

# 一开始以{% extends 'base.html '%}指定要继承的文件为base.html,然后下方以{% block title%}{% endblock %}指定3个区块要填写的内容,其他
# (如<html></html>)共享的标签就不需要了,因为已经在base.html中出现过了,