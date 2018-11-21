前提：
    基于django实现，使用前，你需要
        1.在settings里配置app
        2.在urls里配置site.urls
        3.在app下新建Xadmin.py文件，在下面实现和admin类似的效果

实现内容：

    1.site配置注册和url映射
        n * 4 增删改查url
    
    2.增删改查逻辑和页面
    
        默认 配置Model
        
        增加复选框，编辑，删除按钮
        
        list_display配置: 不配置默认显示， 普通字段显示， 一对多字段显示， 多对多字段显示
        
        list_display_links配置
        
        分页
        
        search搜索
        
        actions批量操作
        
        list_filter关键字筛选
        
        pop功能
        
        支持url扩展
        
        
crm功能：
    讲师与学生
        1.初始化 课程记录和上课记录
        2.考勤(记录--学习记录依据课程记录筛选，action批量设置考勤状态)
        3.录入成绩(跳转新url，编辑框和提交实现)
        4.显示成绩， ajax查询，柱状图显示
        
        5.上传作业(os模块)
        6.下载作用
    
    销售和客户
        1.查询共有客户
        2.查看跟进记录，确认跟进
        3.查看自己的客户
        
        
其他：
    取消课程咨询项
    显示choice字段对应内容
    
    
使用：
    在settings下注册xadmin app  Xadmin.apps.XadminConfig
    在urls下配置url
        from Xadmin.service.xadmin import site
        url(r'^xadmin/', site.urls),
    app下新建Xadmin.py
        from Xadmin.service.xadmin import site
        site.register进行注册表