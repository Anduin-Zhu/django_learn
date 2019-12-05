from django.contrib import admin
from .models import Article,Tags,Category

#
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id','title','created_time',)
#     list_display_links = ('title',)
#
#
# admin.site.register(Article,ArticleAdmin)

# 装饰器注册
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','title','created_time','user','riqi','paixu',)
    list_display_links = ('title',)
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)
    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = ['user']
    # fk_fields 设置显示外键字段
    fk_fields = ['category']
    # 列表顶部，设置为False不在顶部显示，默认为True。
    actions_on_top = True
    # 列表底部，设置为False不在底部显示，默认为False。
    actions_on_bottom = True
    # 定制Action行为具体方法
    def func(self,request,queryset):
        queryset.update(created_time='2019-11-11')

    func.short_description = '更新发布时间'
    actions = [func,]

    # 指定标题title做为搜索字段
    search_fields = ['title',]
    # 右侧栏过滤器，按作者进行筛选
    list_filter = ['user',]
    # 详细时间分层筛选　
    date_hierarchy = 'created_time'

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

# admin.site.register(Tags)
admin.site.register(Category)

# 修改后台管理页面头部显示内容和页面标题
admin.site.site_header = 'Django中文网管理后台'
admin.site.site_title = 'Django中文网'

