from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, FormView, ListView, UpdateView, DetailView
from django.http import HttpResponse, request

from ishot_site.models import Practice, UserProfile
from ishot_site.forms import PracticeForm, ProfileForm

from ishot_site.forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(TemplateView):
    template_name = 'ishot_site/index.html'


def practice_list(request):
    # return HttpResponse('練習一覧')
    practices = Practice.objects.all().order_by('id')
    return render(request, 'ishot_site/practice_list.html', {'practices': practices})


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

    return render(request, 'ishot_site/practice_edit.html', dict(form=form, practice_id=practice_id))


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
        return reverse_lazy('ishot_site:profile_detail', kwargs={'pk': self.kwargs['pk']})

    def form_invalid(self, form):
        messages.success(self.request, 'プロフィールを更新しました。')
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'ishot_site/profile_detail.html'


class ProfileListView(ListView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'ishot_site/profile.html'

    def get_queryset(self):
        profiles = UserProfile.objects.filter(user=self.request.user)

        return profiles

