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
        

bug:
    1.author添加操作报错
    2.添加页面，字段验证错误时，不保留值