from django.urls import path

from .views import BlogListView, AboutPageView, ImputPageView, ModelPageView, ExamplePageView, get_enter,get_register, get_logout

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('imput/', ImputPageView.as_view(), name='imput'),
    path('model/', ModelPageView.as_view(), name='model'),
    path('example/', ExamplePageView.as_view(), name='example'),
    path('enter/', get_enter, name='enter'),
    path('register/', get_register, name='register'),
    path('logout/', get_logout, name='logout')

]
