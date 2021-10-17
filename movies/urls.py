from django.urls import path
from movies.views import *

app_name = 'movies'
urlpatterns = [
    # Template Views
    path('', MovieIndexView.as_view(), name='movie_index_view'),
    path('product_detail/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('search_result/', SearchView.as_view(), name='search_result'),

]
