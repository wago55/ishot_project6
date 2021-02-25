from django.urls import path
from . import views

app_name = 'ishot_site'
urlpatterns = [
    path('index', views.IndexView.as_view(), name="index"),
    path('home', views.HomeView.as_view(), name='home'),
    path('practice/', views.PracticeListView.as_view(), name='practice_list'),
    path('practice/create/', views.PracticeCreateView.as_view(), name='practice_create'),
    path('practice/update/<int:pk>/', views.PracticeUpdateView.as_view(), name='practice_update'),
    path('practice/delete/<int:pk>', views.PracticeDeleteView.as_view(), name='practice_delete'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry_form'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('profile/', views.ProfileListView.as_view(), name='profile_list'),
    path('profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/detail/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
]

