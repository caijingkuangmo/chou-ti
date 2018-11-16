rbac  (Role-Based Access Control)

表：
    用户 <--多对多-->  角色
    角色 <--多对多-->  权限
    
    权限 <--多对一-->  权限组(主要用于前端进行菜单和按钮控制)

流程：
    基于url对表级别的增删改查进行控制
    
    1.登录成功时，获取用户所有权限，注入的session中
    2.下次请求来时，在中间件获取session里的权限，进行校验
    3.前端渲染时，动态生成表管理菜单和可用操作按钮
	
	
使用：
	1.注册app  "rbac.apps.RbacConfig"
	
	2.权限组件User表和公司员工表进行 one2one绑定
	    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
  
	3.python manage.py makemigrations/migrate 生成权限组件表
	
	4.Xadmin组件注册site.reigster权限相关表，添加权限，添加角色，给用户绑定角色，用户表和员工表关联
	
	5.中间件注册权限注入中间件     'rbac.service.rbac.ValidPermission'
	
	6.登录时调用rbac.service.permissions.initial_session(user, request) 把权限注入到session中
	
	7.前端页面继承rbac下的base.html, 当前页面代码放入{% block con %} {% endblock %}下