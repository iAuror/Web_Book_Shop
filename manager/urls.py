from django.urls import path

from manager.views import hello, buy_book

urlpatterns = {
    path('hello/', hello),
    path('hello/<int:digit>', hello),
    path('hello/<str:name>', hello),
    path('book/', buy_book),
}
