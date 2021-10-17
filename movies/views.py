from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.db.models import Q
from movies.models import Movie


class MovieDetail(generic.DetailView):
    template_name = 'movie_temp/movie_detail_view.html'
    model = Movie
    context_object_name = 'movie'


class MovieCardView(generic.DetailView):
    template_name = 'movie_temp/movie_card_view.html'
    model = Movie
    context_object_name = 'movie'


class MovieIndexView(generic.TemplateView):
    template_name = 'movie_temp/movie_index.html'
    extra_context = {
        'movies': Movie.objects.all()
    }


class SearchView(generic.ListView):
    model = Movie
    template_name = 'movie_temp/search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            res = Movie.objects.filter(Q(name__contains=query) | Q(director__contains=query) | Q(description__contains=query))
            result = res
        else:
            result = None
        return result
