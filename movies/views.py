from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic, View
from django.db.models import Q, Avg, Func

from comments.forms import CommentForm
from comments.models import Comment
from movies.models import Movie


class MovieDetail(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        movie = get_object_or_404(Movie, id=pk)
        user = request.user
        comments = movie.comments.all()
        new_comment = None
        comment_form = CommentForm()
        return render(request, 'movie_temp/movie_detail_view.html', {'movie': movie,
                                                                     'comments': comments,
                                                                     'new_comment': new_comment,
                                                                     'comment_form': comment_form})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        user = request.user
        # comments = movie.comments.all()
        # new_comment = None
        user_comment = get_object_or_404(Comment, user=user, movie=movie)
        # Comment posted
        if request.method == 'POST':
            if not user_comment:
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    # Create Comment object but don't save to database yet
                    new_comment = comment_form.save(commit=False)
                    # Assign the current post to the comment
                    new_comment.movie = movie
                    new_comment.user = user
                    # Save the comment to the database
                    new_comment.save()
                return HttpResponseRedirect(reverse_lazy('movies:movie_detail'))
            else:
                return HttpResponse('You already wrote your comment')
        return render(request, 'movie_temp/movie_detail_view.html', {})


class Round2(Func):
    function = "ROUND"
    template = "%(function)s(%(expressions)s::numeric, 2)"


@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    user = request.user
    comments = movie.comments.all()
    new_comment = None
    comment_form = CommentForm()
    if movie.comments.all():
        rating = round(movie.comments.all().aggregate(Avg('rating'))['rating__avg'], 2)
    else:
        rating = 'no rating'
    if request.method == 'POST':
        print(1)
        # user_comment = get_object_or_404(Comment, user=user, movie=movie)
        # if not user_comment:
        if Comment.objects.filter(user=user, movie=movie):
            return HttpResponse('You already wrote your comment')
        else:
            comment_form = CommentForm(data=request.POST)
            print(2)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                print(3)
                print(comment_form.cleaned_data, comment_form)
                # Assign the current post to the comment
                new_comment.movie = movie
                new_comment.user = user
                # Save the comment to the database
                new_comment.save()
        # else:
        #     return HttpResponse('You already wrote your comment')
    return render(request, 'movie_temp/movie_detail_view.html', {'movie': movie,
                                                                 'comments': comments,
                                                                 'new_comment': new_comment,
                                                                 'rating': rating,
                                                                 'comment_form': comment_form})


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
            res = Movie.objects.filter(
                Q(name__contains=query) | Q(director__contains=query) | Q(description__contains=query))
            result = res
        else:
            result = None
        return result
