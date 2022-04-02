from django.shortcuts import render
from .models import New, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator
from .filters import NewFilter
from .forms import NewForm

class News(ListView):
    model = New
    context_object_name = 'news'
    template_name = 'posts.html'
    ordering = ['-dateCreation']
    author = 'authors'
    paginate_by = 5

    def get_filter(self):
        return NewFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class NewDetailView(DetailView):
    template_name = 'news/detail.html'
    queryset = New.objects.all()


class NewCreateView(CreateView):
    template_name = 'news/create.html'
    form_class = NewForm


class NewUpdateView(UpdateView):
    template_name = 'news/create.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)


class NewDeleteView(DeleteView):
    template_name = 'news/delete.html'
    queryset = New.objects.all()
    success_url = '/news/'

# def news_list(request):
#     x = X(request.GET, queryset=New.objects.all())
#     return render(request, 'news_d.html', {'filter': x})


