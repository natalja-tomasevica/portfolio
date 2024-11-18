from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, BookForm
from .models import Author, Book

def home(request):
    return render(request, 'home.html', {})

def data_projects(request):
    return render(request, 'data_projects/data_projects.html', {})

def predicting_stars_galaxies_quasars_project(request):
    return render(request, 'data_projects/predicting_stars_galaxies_quasars_project.html', {})

def user_churn_project(request):
    return render(request, 'data_projects/user_churn_project.html', {})

def predicting_fitness_metrics_project(request):
    return render(request, 'data_projects/predicting_fitness_metrics_project.html', {})

def digital_marketing_campaigns_performance_analysis_project(request):
    return render(request, 'data_projects/digital_marketing_campaigns_performance_analysis_project.html', {})

def django_projects(request):
    return render(request, 'django_projects/django_projects.html', {})

def calculator_project(request):
    if request.method == 'POST':
        result = request.POST.get('result', '')
        return render(request, 'django_projects/calculator_project.html', {'result': result})
    return render(request, 'django_projects/calculator_project.html')

def books_main_page(request):
    return render(request, 'django_projects/books_project/books_main_page.html', {})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            author_full_name = form.cleaned_data['author_full_name']
            author_age = form.cleaned_data['author_age']
            author_languages = form.cleaned_data['author_languages']
            book_title = form.cleaned_data['title']
            book_description = form.cleaned_data['description']
            book_genre = form.cleaned_data['genre']
            book_pages = form.cleaned_data['pages']
            author, created = Author.objects.get_or_create(full_name=author_full_name)
            if created or (author_age and author.age != author_age) or (author_languages and author.languages != author_languages):
                author.age = author_age
                author.languages = author_languages
                author.save()
            
            book = Book.objects.create(title=book_title, author=author, description=book_description, genre=book_genre, pages=book_pages)
            return redirect('book_details', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'django_projects/books_project/add_books_and_authors.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            author_full_name = form.cleaned_data['author_full_name']
            author_age = form.cleaned_data['author_age']
            author_languages = form.cleaned_data['author_languages']
            author, created = Author.objects.get_or_create(full_name=author_full_name)
            if created or (author_age and author.age != author_age) or (author_languages and author.languages != author_languages):
                author.age = author_age
                author.languages = author_languages
                author.save()
                book.author = author
            form.save()
            return redirect('book_details', pk=book.pk)
    else:
        form = BookForm(instance=book, initial={
            'author_full_name': book.author.full_name,
            'author_age': book.author.age,
            'author_languages': book.author.languages,
            'description': book.description
        })
    return render(request, 'django_projects/books_project/edit_book.html', {'form': form})

def edit_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_details', pk=author.pk)
    else:
        form = AuthorForm(instance=author, initial={
            'full_name': author.full_name,
            'age': author.age,
            'languages': author.languages,
        })
    return render(request, 'django_projects/books_project/edit_author.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('all_books_and_authors')
    return render(request, 'django_projects/books_project/delete_book.html', {'book': book})

def delete_author(request, pk):
    author = get_object_or_404(Author, pk = pk)
    if request.method == 'POST':
        author.delete()
        return redirect('all_books_and_authors')
    return render(request, 'django_projects/books_project/delete_author.html', {'author': author})

def all_books_and_authors(request):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    return render(request, 'django_projects/books_project/all_books_and_authors.html', {'all_books': all_books, 'all_authors': all_authors})

def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'django_projects/books_project/book_details.html', {'book': book})

def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    return render(request, 'django_projects/books_project/author_details.html', {'author': author, 'books': books})

def search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains = query) if query else[]
    authors = Author.objects.filter(full_name__icontains = query) if query else[]
    return render(request, 'django_projects/books_project/search.html', {'query': query, 'books': books, 'authors': authors})