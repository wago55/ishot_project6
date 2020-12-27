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
    path('profile/create/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('profile/', views.ProfileListView.as_view(), name='profile_list'),
    path('profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/detail/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
]

