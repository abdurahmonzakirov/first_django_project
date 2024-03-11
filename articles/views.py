from django.http import Http404, HttpResponseRedirect, HttpResponse

from django.urls import reverse

from django.shortcuts import render

from .models import Article


def main_page(request):

    return HttpResponse('<a href="/articles">Статьи</a>')


def index(request):
    latest_articles_list = Article.objects.order_by('id')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')

    latest_comment_list = a.comment_set.order_by('-id')[:15]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')

    a.comment_set.create(author_name = request.GET['Your_name'], comment_text = request.GET['text'])

    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))

