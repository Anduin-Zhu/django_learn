from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog import models

def hello(request):
    return HttpResponse(request.path+request.get_full_path())

def index(request):
    blog_index = models.Article.objects.all().order_by('id')
    context = {
        'blog_index':blog_index,
    }
    return render(request,'blog/index.html',context)

def orm(request):
    '''
    # 增删改

    # 增加一篇文章
    # 方法一
    models.Article.objects.create(title='增加的文章标题1',category_id=3, body='增加内容一', user_id=1)
    # 方法二：添加数据，实例化表类，在实例化里传参为字段和值
    obj = models.Article(title='增加标题二', category_id=2, body='增加内容二', user_id=2)
    obj.save()
    # 方法三：将要写入的数据组合成字典，键为字段值为数据,,,,,,,推荐
    dic = {'title': '增加标题三', 'category_id': '1', 'body': '增加内容三', 'user_id': '1'}
    # 添加到数据库，注意字典变量名称一定要加**
    models.Article.objects.create(**dic)
    # 删除id=6的文章（数据）
    models.Article.objects.filter(id=13).delete()
    # 把标题'增加标题二'，修改成'我被修改了'。将指定条件的数据更新，支持 **kwargs，支持字典。
    models.Article.objects.filter(title='增加标题二').update(title='我被修改了')
    '''
    # 查询
    # 获取所有文章，对应SQL：select * from Article
    all_article = models.Article.objects.all()
    print(all_article)
    return HttpResponse('orm')



