from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']# 可以按照想要的顺序来排列字段
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]# 可以将字段分区域排列
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')# 列表显示的字段
    list_filter = ['pub_date']# 增加一个过滤器
    search_fields = ['question_text']# 增加搜索框



admin.site.register(Question,QuestionAdmin)


