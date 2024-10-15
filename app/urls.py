from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    
    path('data_projects', views.data_projects, name = 'data_projects'),
    
    path('data_projects/predicting_stars_galaxies_quasars_project', views.predicting_stars_galaxies_quasars_project, name = 'predicting_stars_galaxies_quasars_project'),
    path('data_projects/user_churn_project', views.user_churn_project, name = 'user_churn_project'),
    path('data_projects/predicting_fitness_metrics_project', views.predicting_fitness_metrics_project, name = 'predicting_fitness_metrics_project'),
    
    path('django_projects', views.django_projects, name = 'django_projects'),
    
    path('django_projects/calculator_project', views.calculator_project, name='calculator_project'),
    
    path('django_projects/books_project/books_main_page', views.books_main_page, name = 'books_main_page'),
    
    path('django_projects/books_project/all_books_and_authors', views.all_books_and_authors, name='all_books_and_authors'),
    path('django_projects/books_project/add_books_and_authors', views.add_book, name='add_books_and_authors'),
    
    path('django_projects/books_project/book_details/<int:pk>', views.book_details, name = 'book_details'),
    path('django_projects/books_project/author_details/<int:pk>', views.author_details, name = 'author_details'),
    
    path('django_projects/books_project/edit_book/<int:pk>', views.edit_book, name='edit_book'),
    path('django_projects/books_project/edit_author/<int:pk>', views.edit_author, name='edit_author'),
    
    path('django_projects/books_project/delete_book/<int:pk>', views.delete_book, name = 'delete_book'),
    path('django_projects/books_project/delete_author/<int:pk>', views.delete_author, name = 'delete_author'),
    
    path('django_projects/books_project/search', views.search, name = 'search'),
    
]