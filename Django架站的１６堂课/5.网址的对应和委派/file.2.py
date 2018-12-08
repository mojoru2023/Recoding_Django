#　５．２　　高级设置技巧
#　当设计的网站项目越来越大，功能越来越多时，所使用到的网址对应也相对更多，更复杂，运用一些小技巧，可以让程序代码的可读性变得更好
#　另外，有一些多功能的模块会有自己的网址管理设置，学会如何在urlpattern使用include的方法，对于日后在项目中加入这些模块
#　的功能会有很大帮助

#　５．２．１　　参数的传送

#　可以在样式中定义子样式，然后再按序传送给views.py的处理函数，要注意，所有传送过去的参数内容一律是字符串格式，在使用之前可能还需要进行格式转换
#　另外，有时候可能需要一些默认的参数值来降低网址设计的复杂度．例如，在显示关于笔者的时候，如果有指定数字就显示指定的笔者，否则以第０位
#　笔者作为显示的目标，网址的样式可以如下


#　 url(r'about/$',about),
#　 url(r'about/(?P<author_no>([0|1|2|3])/$',about)
#　然后在about函数中自变量行加上一个默认值
from django.conf.urls import include


def about(request,author_no='0'):
    html = "<h2>Here is Authors:{}'s</h2><hr>".format(author_no)
    return HttpReposnse(html)

# 如此,如果网址栏中只指定了/about,那么author_no = '0'就会派上用场,否则就会以在网址中提取到的数字为准(注意,收到是的数据都被视为字符串)
# 除了在子样式中匹配的项目会被当做参数自动传送到views中的处理函数外,如果需要在程序中以手动的方式传送数据过去,那么只要在处理函数后面加上一个字典类型的数据即可

#   url(r'^$',homepage,{'testmode':'YES'}),

# 然后在homepage中就要多设置一个参数(此例中为testmode)用来接收来自于urls.py的自变量.在执行homepage时,参数中的内容就是此例中设置的YES字符串.

# 5.2.2  include其他整组的urlpattern设置
# 大型的网站如果一条一条地设置,将会越来越复杂,到最后不太好维护,所以对于同样性质的网页,可以使用include的方式把urlpatterns放到另一个地方去设置,
# 最常见的方式是:
#  url(r'^admin/',include(admin.site.urls))

#  默认的Django网站的管理网页,针对/admin/开头的内容使用include(admin.site.urls)时,全部交由admin.site.urls处理.事实上在admin的模块中,
# 这行指令就是返回它自定义的urlpattern.特别要注意的是^admin/后面不能加上"$",因为后面还有另外的定义.

# 因此,如果在网站中有一整组由某些文字开头的统一设置,比较正确的做法是先定义自己的urlpatterns,然后使用include的方式加入原有的urlpatterns

my_patterns= [
    url(r'^company/$',company),
    url(r'^sales/$',sales),
    url(r'^contact/$',contact),
]

urlpattersn =[
    url(r'^info/',include(my_patterns)),

]

# 在此例中,我们定义了my_patterns,然后到urlpatterns中把my_patterns使用include指令加入.如此,所有网址中只要是有/info开头的字符串,
# 就会被转送到my_patterns中解析.因此,如localhost:8000/info/company/这样的网址就会调用company函数来加以处理
# 善用include也可以减少重复编写相同的样式.假设要制作一个网站,在网站中每一个产品编号是由4个英文字母和数字所组成的字符串.针对每一个产品,
# 可以有full,medium以及abstract三种显示的方式,用edit进入产品编辑模式,我们可能使用如下编写设置:

#  url(r'^(?P<prod_id> [a-zA-Z0-9]{4})/(?P<mode>full)/$',showp),
#  url(r'^(?P<prod_id> [a-zA-Z0-9]{4})/(?P<mode>medium)/$',showp),
#  url(r'^(?P<prod_id> [a-zA-Z0-9]{4})/(?P<mode>abstract)/$',showp),
#  url(r'^(?P<prod_id> [a-zA-Z0-9]{4})/(?P<mode>edit)/$',showp),


# 显然,前面对于产品编号的样式设置都是重复的,因此我们可以把它改写如下:


url(r'^(?P<prod_id>[a-zA-Z0-9]{4})/',
    include(
        [
            url(r'^(?P<mode>full)/$',showp),
            url(r'^(?P<mode>medium)/$',showp),
            url(r'^(?P<mode>abstract)/$',showp),
            url(r'^(?P<mode>edit)/$',showp),

        ]
    ))

# 5.2.3   URLconf的反解功能


# 前面的内容都在说明如何设计好的pattern来验证网址是否是我们需要的样子,那么反过来,如果我们要在网页中建立链接,也可以运用设计好的pattern
# 来产生匹配格式的网址,而且非常简单.在使用之前,必须先对设计好的样式取一个名字,只要在url()函数中加上name的命名即可,如下

#  url(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,3})$',post,name='post-url')

# 我们以之前设置要显示文章内容的样式为例,在此把它命名为post-url,她会有4个子样式的参数.接着,如果我们要在网页中的html文件中按此格式编出
#　网址蓝，在模板文件(此例子为index.html)
#  其中,{% url 'post-url' 2018 12 6 01%}这一行表示要以(2018,12,06,01)这4个数字为自变量,找到刚刚在urls.py中的设置重新编写
#  付出和匹配该样式的格式,如下  /post/2018/12/6/1

# 如果要让此网址成为链接,那么把刚刚那一行更改如下

