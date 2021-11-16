from django.urls import path
from .views import home, results, print_db

urlpatterns = [
    path('', home, name='home'),
    path('results/', results, name='results'),
    path('print_db/', print_db, name='print_db')
]
