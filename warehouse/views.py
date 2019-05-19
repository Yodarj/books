'''views'''

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def homepage(request):
    '''rendering function'''
    return render(request=request,
                  template_name='warehouse/home.html',
                  context={'books': Book.objects.all()})

def listpage(request):
    '''rendering function'''
    return render(request=request,
                  template_name='warehouse/list.html',
                  context={'books': Book.objects.all()})

def addpage(request):
    '''rendering function'''
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/added/")
    form = BookForm
    return render(request=request,
                  template_name='warehouse/add.html',
                  context={'form':form})

def importpage(request):
    '''rendering function'''
    book = {}
    if 'key_word' in request.GET:
        key_word = request.GET['key_word']
        url = 'https://www.googleapis.com/books/v1/volumes?q=%s' % key_word
        response = request.get(url)
        book = response.json()
        book = book.get("items")
    return render(request,
                  template_name='warehouse/import.html',
                  context={'book': book})

def bookaddedpage(request):
    '''rendering function'''
    return render(request=request,
                  template_name='warehouse/bookadded.html',
                  context={'books': Book.objects.all()})

def search(request):
    '''search function'''
    template = 'warehouse/list.html'

    query = request.GET.get('q')

    if query:
        results = Book.objects.filter(Q(title__icontains=query) |
                                      Q(authors__icontains=query) |
                                      Q(categories__icontains=query))
    else:
        results = Book.objects.all()


    context = {'books':results}

    return render(request, template, context)

# class IndexView(generic.ListView):
#     template_name = 'warehouse/header.html'
#     page_template = 'warehouse/all_movies.html'
#     context_object_name = 'books'
#     model = Book

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context.update({
#             'all_books': Book.objects.all(),
#             'page_title': 'Najnowsze'
#         })
#         return context

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             return Book.objects.filter(title__icontains=query)
#         else:
#             return Book.objects.all()
