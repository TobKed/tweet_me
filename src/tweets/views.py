from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from .models import Tweet


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/tweet_create_form.html"
    success_url = "/tweet/"


class TweetDetailView(DetailView):
    model = Tweet


class TweetListView(ListView):
    model = Tweet


def tweet_detail_view(request, pk):
    obj = Tweet.objects.get(id=pk)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
