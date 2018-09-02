from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
from django.urls import reverse

#���׸���: jango���� �����ϴ� �������� ����� �ϴ� ��Ŭ����
#class ���̸�(���׸���):
#ListView: Ư�� ��ü�� ����� �ٷ�� ����� ���� ���׸���

from django.views.generic.list import ListView
#obj = Post.object.all()
#render(request, 'blog/index.html', {'obj':obj})

class index(ListView):
    #template_name: html������ ��θ� ���ڿ��� ���� ����
    template_name = 'blog/index.html'
    #model: � ��Ŭ������ ��ü�� ����Ʈ���Ұ��� ����ϴ� ����
    model = Post
    #context_object_name: ���ø����� ����� ��ü ����Ʈ�� ������ ������
    context_object_name = 'list'
    #paginate_by: �� �������� �� ���� ��ü�� �������� �����ϴ� ����
    paginate_by = 5
    
def detail(request, post_id):
    obj = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/detail.html", {'post':obj})
    
    
def searchP(request):
    #<input type="text" name="query"/>
    #GET��û���� �� �����Ϳ��� name�Ӽ��� 'query'�� ������ ����
    #name�Ӽ��� 'query'�� �Ӽ��� ������ �⺻�� '' ��ȯ
    q = request.GET.get('query', '')
    t = request.GET.get('type',)
    #'0': ����˻�
    if t == '0':
        #Post.objects.filter(����): Ư�������� �����ϴ� Post ��ü ����
        #filter, exclude, get�Լ� ����: ��Ŭ���� ������ ������ ������__��ɾ� = ��
        #contains: �캯���� �ش��ϴ� ���ڿ��� �ش� ��ü�� ������ ����Ǿ��ִ��� Ȯ��
        list = Post.objcets.filter(headline__contains=q)
        return render(request, 'blog/searchP.html',{'list':list})
    #'1': ����˻�
    elif t == '1':
        Post.objects.filter(content__contains=q)
        return render(request, 'blog/searchP.thml',{'list':list})
    
    



