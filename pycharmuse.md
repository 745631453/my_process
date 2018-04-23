通过练习命令来执行一些操作避免老是通过图形化操作，忘记最笨来的代码

[toc]

# 安装虚拟环境

## 1. window cmd下安装
pip install virtualenv
> 查看安装所有环境的路径方式：
> path

## 2. 创建env环境（建立虚拟环境）
1. virtualenv --no-site-packages -p（如果有别的版本的python那么需要-p后面跟你指定要用到python的路径)  文件名
2. 进入环境里 cd scipts文件下 输入
>acrivate/deactivate 开启环境/关闭文件

## 安装django
>pip install django==1.11 （‘==’后面表示版本号）

如果是在命令模式下需要进入虚拟环境在cd至你创建的django目录下
**每一个django都需要单独的虚拟环境，避免数据重合——因此在pycharm中也是需要每个项目启一个单独虚拟环境**

1. 创建Django工程
>django-admin startproject  文件名

2. 启动django工程
>python marange.py runserver 8008（表示自己设置的端口可以是任意的）

3. 创建app
>python manage.py startapp 

## 修改django配置
修改中文：
进入settings.py文件后
找到修改LANGUAGE_CODE = 'zh-hans'
UTC时间是早8小时
所以TIME_ZONE改为Asia/Shanghai
在系统给你的ip地址下就可以进入该页面
![这里写图片描述](https://img-blog.csdn.net/20180423201414664?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNzgxODc3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
# pychram下操作django
前面说道每个django项目都是单独的虚拟环境变量下操作的因此每次启动都需要在不同的虚拟环境下安装django
由于pycharm只带虚拟环境这个我们不过多解释，我们只需要来一场比较复杂的配置虚拟环境的方式
## 配置外部虚拟环境
在设置中配置porject 右上角add添加 existing environmrnt 选择自己配置的env—— 可以节省cmd中打开进入步骤
## 配置django
在左上角找到run中debug 创建script path中 找到创建的django中的——manage.py
然后在Parameters中 runserver 8800（自己设置的端口）
这样有节约了启动django的的步骤
在创建出来的django目录下有
__init__.py表示初始的设定由于在python3中需要特别设置数据库所哟需要写入
```
import pymysql

pymysql.install_as_MySQLdb()
```
settings.py文件下设置各种变量其中包括链接mysql的代码：
```
INSTALLED_APPS=[中需要添加创建的app的名称]
DATABASES = {
    'default': {
    	        'ENGINE':'django.db.backends.mysql',
		'NAME':'',           #数据库名
		'USER':'',           #账号
		'PASSWORD':'',       #密码
		'HOST':'127.0.0.1',  #IP(本地地址也可以是localhost)
		'PORT':'3306',       #端口
		    }
		    }
		    ```
		    urls.py文件配置的是指定用户输入的url来呈现不同的效果因此需要配置在app中的url
		    该页面就类似与不同目录下打开后有不同的效果
		    ```lpatterns = [
		        url(r'^admin/', admin.site.urls),
			    url(r'app/',include('app.urls')),
			        url(r'stu/',include('stu.urls'))
				]
				#其中r中表示的是url的后缀名 include跟的是app中的urls文件
				```
				## 创建app以及初步的运用
				在pycharm中左下角找到Terminal在里面输入命令创建app项目
				其中app文件下
				>__init__.py:初始化
				admin.py: 管理后台注册模型
				apps.py: settings.py里面注册app的时候需要使用到。一般不推荐这样使用INSTALLED_APPS中
				from app.apps import AppConfig
				AppConfig.name
				models.py: 写模型的地方
				views.py: 写处理业务逻辑的地方

				## app创建链接给mysql添加数据

				在models.py 中配置方式
				```
				class Student(models.Model):

				s_name = models.CharField(max_length=10)
				s_age = models.IntegerField()
				s_gender = models.BooleanField()

				class Meta:
				    db_table = 'cd_student'（列表名）
				        ordering =[]
					对象的默认排序字段，获取对象列表时使用，升序ordering['id']，降序ordering['-id']
					```
					在urls.py中创建的是用户视角的引用是关联views.py文件的
					```
					from stu.models import Student


					def main(request):
					    return HttpResponse('你好')

					    def addStudent(request):
					        stu = Student()
						    stu.name = 'coco'
						        stu.sex = 1

							    stu.save()
							        return HttpResponse('添加成功')
								```

								```
								from django.conf.urls import url

								from stu import views

								urlpatterns = [
								    url(r'hello/',views.main),
								        url(r'addstudent',views.addStudent)
									]

									```
									表示了如果用户输入了addstudent的时候出现的添加成功界面同时也添加到了mysql数据库中
									当然在此之前需要配置一下文件迁移
									## 迁移数据库
									1. 生成迁移文件

									>python manage.py makemigrations

									注意：如果执行后并没有生成迁移文件，一直提示No changes detected这个结果的话，就要手动的去处理了。有两点处理方式： 1） 先删除掉__pycache__文件夹 2） 直接强制的去执行迁移命令，python manage.py makemigrations xxx (xxx就是app的名称) 3） 查看自动生成的数据库，查看表django_migrations，删掉app字段为xxx的数据(xxx就是app的名称)
									2. 执行迁移生成数据库

									>python manage.py migrate
									此时就生成了数据可一看到生成的许多列表

									注意: 生成迁移文件的时候，并没有在数据库中生成对应的表，而是执行migrate命令之后才会在数据库中生成表


