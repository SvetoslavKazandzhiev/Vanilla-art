from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.base import View

from artportal.art_app.forms import EditArtForm, CommentForm
from artportal.art_app.models import Art, Comment


class IndexView(ListView):
    template_name = 'index.html'
    model = Art
    context_object_name = 'arts'
    paginate_by = 9


class CreateArtView(LoginRequiredMixin, CreateView):
    model = Art
    fields = ('name', 'description', 'image', 'type',)
    success_url = reverse_lazy('index')
    template_name = 'create.html'

    def form_valid(self, form):
        art = form.save(commit=False)
        art.user = self.request.user
        art.save()
        return super().form_valid(form)


class DeleteArtView(DeleteView):
    template_name = 'art/art-delete.html'
    model = Art
    success_url = reverse_lazy('index')


class ArtDetailsView(LoginRequiredMixin, DetailView):
    model = Art
    template_name = 'art/art-details-img.html'
    context_object_name = 'art'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        art = context['art']
        is_owner = art.user == self.request.user
        context['comment_form'] = CommentForm(
            initial={
                'art_pk': self.object.id,
            }
        )
        context['comments'] = art.comment_set.all()
        context['is_owner'] = is_owner

        return context


class CommentArtView(LoginRequiredMixin, View):
    form_class = CommentForm
    get_success_url = ''

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        art = Art.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            art=art,
            user=self.request.user
        )
        comment.save()
        return redirect('details art img', art.id)

    def form_invalid(self, form):
        pass


def edit_art(request, pk):
    art = Art.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditArtForm(request.POST, instance=art)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditArtForm(instance=art)
    context = {
        'art': art,
        'form': form,
    }
    return render(request, 'art/art-edit.html', context)
