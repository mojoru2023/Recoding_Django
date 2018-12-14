# 2.4  高级网站功能的运用

# 一个成熟的博客网站,除了前面所设计的功能外,还需要具备显示图形的功能.首页的设计也需要有版面的概念.此外,在文章内容的编排方面,给编写这
# 提供简易排版的功能,可以在文章中设计版面,插入图形以及建立链接等


# 2.4.1   javascript以及css文件的引用


# 一个网站不可能从无到有一点一点自行编辑设计,大部分都是使用现成的网页框架,直接套用并加以修改完成的. Bootstrap是常用的网页框架,单击箭头
# 所指的地方,把CDN的链接复制下来,然后放到base.html模板文件中(加在<head>前面即可),接着在所有模板文件中都可以使用Bootstrap的功能

# 例如, 可以在header.html中使用well大标题格式
# 然后,在base.html中使用Panel来安排首页的外观
# 接着引入Boostrap的Grip概念,通过row和col的设置做出一般博客网站侧边的效果,同样是在base.html中修改,内容如下 (仅显示<body></body>中的内容)

# 我们使用<div class='row'>和<div class='col-md-xx'>的搭配让左侧边栏占用4个格子(Bootstrap把屏幕的横向分格为12个格子),内文的部分占用
# 8个格子,接着在各自的中使用panel创建其内容.


# 2.4.2  图像文件的应用

# 一般来说,网站的图像文件大部分被放置在image文件夹下,.css和.js文件会被分别放在css和js文件夹下.Django把和类型的文件从通常为static files(静态文件)
# 为了能够在网站中顺利存取这些文件,首先要在settings.py中特别指定静态文件要放置的位置.统一将一些文件(.js,.css,.jpg,.png等)放在static的文件家下

# .js放在js子目录,.css放在css子目录,图像文件则放在images子目录中.

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]


#  从os.path.join(BASE_DIR,'static')可以得知,static位置也在网站的文件夹中,其位置和templates文件夹是平行的.接着把网站中要用到的logo文件
# logo.png放在static/images下,到header.html中加入对图像文件的存取操作

#　注意，文件的第２行(% load staticfiles %)只需要使用一次，提醒Django加载所有静态文件备用，这行指令在同一个文件中使用一次即可
#　在真正导入图像文件的地方，使用{% static 'images/logo.png'%}模板语言，Django会按照当时的执行环境把这个文件的可存取网络地址传送给浏览器
#　在header.html中把原来的欢迎文字标题改为logo.png图像文件
#　同样的方法也是用与自定义的css文件以及.js文件的存取


#　２．４．３　　在主网页显示文章摘要

#　在博客网站中有一个特殊，就是要显示这篇文章的摘要．显示摘要一般有两种方式：

#　１．　一种直接在数据库定义的时候，在建立Model的时候把摘要数据加进去，让版主在创建晚装的时候就可以输入摘要，然后在template中把它显示出来
#　２．　第二种，就是根据文章的内容会直接提取前面固定字数的字符，把它们另外显示出来


#　之前，我们在template文件中要输入变量中的数据，都是以{{ post.title }}的方式，把变量额内容按照原来额样子显示出来，其实在输出前还有filter过滤器
#　可以使用，指定过滤器放的方式就是在变量后面加上国内"|" (例如， {{ post.title | filter_command }})

#　 显示的首页文章中可以列出摘要，显然要使用truncatechars这个filter.也要显示出每一篇文章的发布时间，可以通过date这个filter来调整
#　日期时间格式．除此之外，改进后的主页希望可以让每篇文章的标题，摘要以及发布时间有整体感，因为它们属于同一篇文章的３个显示项目，此时通过Bootstrap
#　中的Panel设置，分别设置为Panel的heading.body,以及footer.此外，我们在Panel中使用css指令设置背景颜色，让每篇文章能够进行区分．重新设计后的index.html

#　２．４．４　　博客文章的HTML内容处理


#　　文章中所用到的图像文件从第三放图像文件服务网站(例如imgur.com)获取为主．所有张贴文章所需要的图像文件，在处理后(包括图像尺寸，水印以及版权声明等)
#　上传到该网站，在取得链接后再放到我们的文章中．获取这个信息后(以HTML),增加博客文章时，可在适当的地方直接粘贴此段HTML程序代码
#　使用admin页面新增文章时，加入HTML代码片段．单击"保存"按钮后，此程序代码会被原封不动的保存在网站的数据库中，

#　django在默认情况下不随便解析HTML代码的．主要是网络完全的问题．由于这是我们自己的博客网站，并不开放其他人来添加数据或资料，因此只要
#　在post.html中输出post.body的后面加上一个safe的过滤器即可

{{ post.body | safe }}

#　加上safe后，此文章内所有HTML代码就被这哪里解读出来，当然我们放你赶紧去图像文件也可以顺利地显示在文章中

#　同理，其他(如css)设置也可以通过此方式加上去，因此可以在文章中自由地使用HTML和css做出自己想要的排版内容

#　２．４．５　　Markdown  语句解析与应用

#　使用Markdown语句，让博客在编辑文章的时候可以兼顾弹性，便利性和安全性

# 安装django-markdown-deux   pip  install django-markdown-deux

# 接着settings.py的INSTALLED_APP段落中,把markdown_deux加进去

# 再到我们解析Markdown语句的post.html中加载Markdown语句标记以及过滤器,

#　最重要的是{% extends ...%}的下一行加载markdown_deux__tagx，在真正文章的地方把原来的safe过滤器置换为markdown,村盘后，把原来的
#　文章内容加上简单的Markdown,