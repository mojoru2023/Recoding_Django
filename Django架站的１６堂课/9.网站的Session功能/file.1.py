#  第9章  网站的session功能


#  在浏览器中记住同一个用户的方法,一般都是使用session(会话阶段).本章介绍如何在django网站中使用session的特性提升网站的功能


#  9.1  session 简介

#  9.1.1  复制django网站

#  grep指令找出和项目有关的字符串,然后修改名称即可

#  9.1.2  cookie简介

#  使用django设计的网站,也可以使用cookie来检查这个浏览器的请求者是否曾经访问过我们的网站,在视图函数中设置


def index(request,pid=None,del_pass=None):
    tempalte = get_template('index.html')
    if request.session_test_cookie_worked():
        request.session.delete_test_cookie()
        message = 'cookie supported~'

# 9.1.3  使用cookie建立网站登录功能

#  9.1.4 开始使用session

#  session把所有数据放在服务端,客户端只会记录一个识别的信息.默认django的session后端会使用到数据库,而主要的操作也可以选择使用cookie-based
#  和file-based的方法是.

#  9.2  活用 session

#   9.2.1  建立用户数据表
#  注意会员网站的逻辑, 前后端的结合

#  9.2.2  整合Django的信息显示框架messages framework

