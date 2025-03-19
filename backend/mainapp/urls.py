from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page, name='home'),
    path('home/', views.index_page, name='home'),
    path('words_list/', views.words_list, name='words_list'),
    path('add_word/', views.add_word, name='add_word'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)