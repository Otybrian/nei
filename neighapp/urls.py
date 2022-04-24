from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'profile/', views.profile, name='profile'),
    url('createHood/', views.create_neighbourhood, name='createHood'),
    url('joinhood/<id>', views.join_neighbourhood, name='joinhood'),
    url('leavehood/<id>', views.leave_neighbourhood, name='leavehood'),
    url('singleHood/<hood_id>', views.single_neighbourhood, name='singleHood'),
    url('<hood_id>/post/', views.create_post, name='post'),
    url('<hood_id>/business/', views.add_business, name='business'),
    url(r'^searchbusiness/', views.search_business, name='search'),
]
