from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, FormView, ListView, UpdateView, DetailView, DeleteView
from django.http import HttpResponse, request

from ishot_site.models import Practice, UserProfile
from ishot_site.forms import PracticeForm, ProfileForm

from ishot_site.forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomeView(ListView, LoginRequiredMixin):
    template_name = 'ishot_site/home.html'

    def get_queryset(self):
        profile = UserProfile.objects.filter(user=self.request.user)
        return profile


class IndexView(TemplateView):
    template_name = 'ishot_site/index.html'


class PracticeListView(ListView, LoginRequiredMixin):
    model = Practice
    template_name = 'ishot_site/practice_list.html'

    def get_queryset(self):
        practice = Practice.objects.order_by('id')

        return practice


class PracticeCreateView(CreateView, LoginRequiredMixin):
    model = Practice
    template_name = 'ishot_site/practice_create.html'
    form_class = PracticeForm
    success_url = reverse_lazy('ishot_site:practice_list')

    def form_valid(self, form):
        practice = form.save(commit=False)
        practice.user = self.request.user
        practice.save()
        messages.success(self.request, '練習の作成が完了しました。')
        return super().form_valid(form)


def practice_edit(request, practice_id=None):
    # return HttpResponse('練習の編集')
    if practice_id:
        practice = get_object_or_404(Practice, pk=practice_id)
    else:
        practice = Practice()

    if request.method == 'POST':
        form = PracticeForm(request.POST, instance=practice)
        if form.is_valid():
            practice = form.save(commit=False)
            practice.save()
            return redirect('ishot_site:practice_list')
    else:
        form = PracticeForm(instance=practice)

    return render(request, 'ishot_site/practice_create.html', dict(form=form, practice_id=practice_id))


class PracticeUpdateView(UpdateView, LoginRequiredMixin):
    model = Practice
    template_name = 'ishot_site/practice_update.html'
    form_class = PracticeForm
    success_url = reverse_lazy('ishot_site:profile_list')

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールを更新しました。')
        return super().form_valid(form)


class PracticeDeleteView(DeleteView, LoginRequiredMixin):
    model = Practice
    template_name = 'ishot_site/practice_delete.html'
    success_url = reverse_lazy('ishot_site:practice_list')


def practice_del(request, practice_id):
    # return HttpResponse('練習の削除')
    practice = get_object_or_404(Practice, pk=practice_id)
    practice.delete()
    return redirect('ishot_site:practice_list')


class InquiryView(FormView):
    template_name = 'ishot_site/inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('ishot_site:inquiry_form')

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)


class ProfileCreateView(CreateView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'ishot_site/profile_create.html'
    form_class = ProfileForm
    success_url = reverse_lazy('ishot_site:profile_list')

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        messages.success(self.request, 'プロフィールの更新が完了しました。')
        return super().form_valid(form)


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'ishot_site/profile_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('ishot_site:profile_list')

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールを更新しました。')
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'ishot_site/profile_detail.html'


class ProfileListView(ListView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'ishot_site/profile_list.html'

    def get_queryset(self):
        profiles = UserProfile.objects.filter(user=self.request.user)

        return profiles
