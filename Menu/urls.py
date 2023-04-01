from django.urls import path
from .views import index

urlpatterns = [
    path('', index, {'name': 'Главная'}, name='main'),
    path('about', index, {'name': 'О нас'}, name='about'),
    path('worldChampions/', index, {'name':'Чемпионы мира'}, name='world_champions'),
    path('worldChampions/first', index, {'name': 'Вильгельм Стейниц'}, name='first'),
    path('worldChampions/second', index, {'name':'Эмануэль Ласкер'}, name='second'),
    path('games', index, {'name': 'Партии великих шахматистов'}, name='games'),
    path('Garry/', index, {'name':'Партии Гарри Каспарова'}, name='Garry'),
    path('KasparovVSKarpov', index, {'name': 'Матч за звание чемпиона мира по шахматам 1984/1985'}, name='firstMatch')
]
