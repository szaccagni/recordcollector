from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_detail, name='detail'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_review', views.add_review, name='add_review'),
    path('records/<int:record_id>/add_photo/',views.add_photo, name='add_photo'),
    path('records/<int:record_id>/add_genre/<int:genre_id>/', views.add_genre, name='add_genre'),
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genre_detail'),
    path('sellers/', views.SellerList.as_view(), name='sellers_index'),
    path('sellers/create/', views.SellerCreate.as_view(), name='sellers_create'),
    path('sellers/<int:pk>/', views.SellerDetail.as_view(), name='sellers_detail'),
    path('sellers/<int:seller_id>/add_price', views.PriceCreate.as_view(), name='price_create'),
]
 