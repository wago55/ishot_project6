from django.forms import ModelForm
from django import forms
from ishot_site.models import Practice, Inquiry, UserProfile
from django.core.mail import EmailMessage


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = (
            'date', 'place', 'place_url', 'start_time', 'finish_time',
        )


class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = (
            'name', 'email', 'title', 'message',
        )

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = f'お問い合わせ {title}'
        message = f'送信者名: {name}\nメールアドレス: {email}\nメッセージ: {message}'
        from_email = 'admin@gmail.com'
        to_list = [
            'test@gmail.com'
        ]
        cc_list = [
            'email'
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email,
                               to=to_list, cc=cc_list)

        message.send()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'last_name', 'first_name', 'sex', 'old', 'university',
            'grade', 'experience'
        )