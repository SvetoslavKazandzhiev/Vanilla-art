from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, FormView

from artportal.art_app.models import Art
from artportal.art_auth.forms import LoginForm, RegisterForm, AccountForm
from artportal.art_auth.models import Account
from artportal.core.mixins import BootStrapFormViewMixin


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)


class RegisterView(BootStrapFormViewMixin, CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


def logout_user(request):
    logout(request)
    return redirect('index')


class AccountDetailsView(LoginRequiredMixin, FormView):
    template_name = 'auth/user_profile.html'
    form_class = AccountForm
    success_url = reverse_lazy('view profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Account.objects.get(pk=self.request.user.id)
        return super().get(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Account.objects.get(pk=self.request.user.id)
        return super().post(request,*args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['arts'] = Art.objects.filter(user_id=self.request.user.id)
        context['account'] = self.object
        return context


User = get_user_model()


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('index')
    template_name = 'profiles/user-confirm-delete.html'


