[otc]
# 简介
ngo是一个开放源代码的Web应用框架，由Python写成。采用了MTV的框架模式，即模型M，模板T和视图V。
Django是一个基于MVC构造的框架。但是在Django中，控制器接受用户输入的部分由框架自行处理，所以 Django 里更关注的是模型（Model）、模板(Template)和视图（Views），称为 MTV模式。它们各自的职责如下：
层次
职责
模型（Model），即数据存取层
处理与数据相关的所有事务： 如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。
模板(Template)，即业务逻辑层
处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。
视图（View），即表现层
存取模型及调取恰当模板的相关逻辑。模型与模板的桥梁。


# 安装虚拟环境（windows）
pip install virtualenv

## 查看安装的所有环境的路径
path

# 创建env环境
virtualenv --no-site-packages -p(如果有别的版本的python那么需要-p后面跟你指定要用到python的路径) 文件名

## 进入环境
cd scripts 然后输入命令avrivate 进入环境/deactivate 退出

# 安装djanggo
pip install django==1.11 ('=='表示版本号)
由于在虚拟环境装的jgango所以打开后需要cd进入项目文件里

创建Django
djiango-admin startproject 文件名

进入文件名后打开
python marange.py runserver

修改中文：进入settings.py文件后
找到修改LANGUAGE_CODE = 'zh-hans'