from django.views.generic import ListView
from .models import Article
from django.shortcuts import redirect, render

class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"



def dashboard(request):
    total_articles = Article.objects.count()
    articles_en_stock = Article.objects.filter(quantity__gt=0).count()
    stock_faible = Article.objects.filter(quantity__lte=5).count()
    return render(request, 'dashboard.html', {
        'total_articles': total_articles,
        'articles_en_stock': articles_en_stock,
        'stock_faible': stock_faible,
    })

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/liste_articles.html', { 'articles': articles })



def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'Article/ajouter_article.html', {'form': form})

def modifier_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'articles/modifier_article.html', {'form': form})

# views.py

def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail_article.html', {'article': article})

# views.py

def supprimer_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('liste_articles')
