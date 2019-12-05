from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.utils import timezone
from django.views import generic

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'polls/index.html',context)# 载入模板，填充上下文，再返回由它生成的 HttpResponse 对象

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        返回最后五个已发布的问题(不包括未来的时间发布的)
        :return:
        """
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def detail(request,question_id):
    """
    显示指定投票的问题标题
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question,pk=question_id)# 尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误
    '''
    为什么我们使用辅助函数 get_object_or_404() 而不是自己捕获 ObjectDoesNotExist 异常呢？
    还有，为什么模型 API 不直接抛出 ObjectDoesNotExist 而是抛出 Http404 呢？
    因为这样做会增加模型层和视图层的耦合性。指导 Django 设计的最重要的思想之一就是要保证松散耦合。
    一些受控的耦合将会被包含在 django.shortcuts 模块中。
    '''
    return render(request,'polls/detail.html',{'question':question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

