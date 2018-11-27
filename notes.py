



#批量创建py文件(linux命令)

#touch file.{1..5}.py




#批量创建文件夹
import os

themes = ['1.网站开发环境的建立','2.Ｄjango网站快速入门','3.让网站上线','4.深入了解Django的MVC架构','5.网址的对应和委派','6.Template深入探讨','7.Models与数据库','8.网站窗体的应用','9.网站的Session功能','10.网站用户的注册与管理','11.社交网站应用实践','12.电子商店网站实践','13.全功能电子商店网站django-oscar实践','14.二级网络域名管理网站实践','15.名言佳句产生器网站实践','16.课程回顾与下一步']
base = "/home/karson/Recoding_Django/Django架站的１６堂课/"
for i in themes:
    file_name = base + str(i)
    os.mkdir(file_name)