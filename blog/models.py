from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    然后给name设置了一个'分类'的名称
    """
    name = models.CharField('分类',max_length=100)

    class Meta:
        """
        Meta是一个内部类，它用于定义一些Django模型类的行为特性
        """
        # db_table = "table_name"# 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        # index_together = [('pub_date','deadline'),]# 联合索引
        # unique_together = (("driver", "restaurant"),)# 联合唯一索引

        verbose_name = '分类'# admin中显示的表名称
        verbose_name_plural = verbose_name# 显示以这个选项为准

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField('标签',max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    objects = models.Manager()
    title = models.CharField('标题', max_length=70)
    # 使用 TextField 来存储大段文本，文章摘要，我们指定了最大长度和允许可以为空。
    intro = models.TextField('摘要', max_length=200, blank=True)
    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 category 指定了 blank=True。
    # 文章分类，我们还使用了on_delete参数，这个是Django2.0强制ForeignKey必须使用的。
    # 具体更多的资料可以查看官网，也可以查看Django2.0外键参数on_delete的使用方法：https://www.django.cn/article/show-6.html
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类',default='1')
    tags = models.ManyToManyField(Tags,blank=True)
    body = models.TextField('内容', max_length=1000, blank=True)
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    # created_time，我们使用了DateTimeField字段，添加了一个auto_now_add参数，自动获取添加时间！
    created_time = models.DateTimeField('发布时间',auto_now_add=True)

    #列可以是模型字段，还可以是模型方法，要求方法有返回值。通过设置short_description属性，可以设置在admin站点中显示的列名。
    def riqi(self):
        return self.created_time.strftime("%b %d %Y %H:%M:%S")
    # 设置方法字段在admin中显示的标题
    riqi.short_description = '发布日期'
    # 指定排序依据
    riqi.admin_order_field = 'created_time'

    # 定义关联对象字段
    def paixu(self):
        return self.category.name

    paixu.short_description = '分类排序'
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

