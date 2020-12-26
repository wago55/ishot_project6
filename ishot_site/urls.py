from django.urls import path
from . import views

app_name = 'ishot_site'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('practice/', views.practice_list, name='practice_list'),
    path('practice/add', views.practice_edit, name='practice_add'),
    path('practice/mod/<int:practice_id>/', views.practice_edit, name='practice_mod'),
    path('practice/del/<int:practice_id>', views.practice_del, name='practice_del'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry_form'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
