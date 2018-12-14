# 7.3  在django中使用mysql数据库系统

# 7.3.1   安装开发环境中的mysql连接环境


# 步骤1  在开发环境中安装mysql服务器
# 步骤2 安装Python和mysql之间的连接驱动程序
# 步骤3  修改settings.py中的设置,提供mysql的链接信息
# 使用mysql这个默认的mysql交互式操作界面,登录再使用"create database mydb"创建一个稍后在django网站中要使用的数据库mydb(名称可以自定义)

# 此时,再执行python manage.py makemigrations以及 python manage.py migrate 指令,django就会连接本地的数据库,登录后,把当前所有数据库的
# 数据表结构重新在本地的mysql数据库中创建一遍,当然此时所有的数据并不会带过去,如果需要把现有的数据带过去,就要使用sql导入和导出的操作

#