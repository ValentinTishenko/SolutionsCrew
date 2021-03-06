import math
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from cactusproj.accounts.models import Profile
from cactusproj.core.models import Problem
from .forms import ProblemCreateForm


class MainPageView(LoginRequiredMixin, CreateView):
    template_name = 'landing/main_page.html'
    form_class = ProblemCreateForm

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        form.instance.description = 'description blah'
        form.instance.location = 'location'
        # adding points to user
        self.request.user.profile.points += 2
        self.request.user.profile.level = int(math.log(self.request.user.profile.points, 2))
        self.request.user.save()
        return super(MainPageView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, _('Problem created successfully'))
        return reverse_lazy('landing:main_page')


class MapPageView(LoginRequiredMixin, TemplateView):
    template_name = 'landing/map_page.html'

    def get_context_data(self, **kwargs):
        context = super(MapPageView, self).get_context_data(**kwargs)
        context['problems'] = Problem.objects.active()
        return context


class ProblemDetailView(LoginRequiredMixin, DetailView):
    model = Problem
    template_name = 'landing/problem_detail.html'


class FeedPageView(LoginRequiredMixin, TemplateView):
    template_name = 'landing/feed_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FeedPageView, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.order_by('-points')
        return context
