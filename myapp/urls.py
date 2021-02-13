from django.urls import path, re_path
from myapp import views as myapp_views
# from myapp.views import StaticView
from django.views.generic import *
from myapp.models import *

urlpatterns = [
    re_path(r'^$', myapp_views.welcome, name='welcome'),
    # re_path('viewArticle/(\d+)/', myapp_views.viewArticle, name='viewArticle'),
    path('viewArticleId/<articleId>/', myapp_views.viewArticleId, name='articleId'),
    path('viewArticle/<int:year>/<int:month>', myapp_views.viewArticle, name='article'),
    path('crudops/', myapp_views.crudops, name='crud'),
    path('datamanipulation/', myapp_views.datamanipulation, name='datamanipulation'),
    path('sendSimpleEmail/<str:emailto>', myapp_views.sendSimpleEmail, name='sendSimpleEmail'),
    # path('static/', StaticView.as_view(template_name = 'static.html'), name='static'),
    path('static/', TemplateView.as_view(template_name = 'static.html'), name='static'),
    path('dreamreals/', ListView.as_view(model = Dreamreal, template_name = "list.html"), name='dream'),
    path('connect/', TemplateView.as_view(template_name = 'login.html'), name='conect'),
    path('login/', myapp_views.login, name='login'),
    path('profile/', TemplateView.as_view(template_name = 'profile.html'), name='profile'),
    path('saved/', myapp_views.SaveProfile, name='saved'),
    path('profileData/', ListView.as_view(model = Profile, template_name = "list.html"), name='dream'),







]
