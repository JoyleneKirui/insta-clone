from django.urls import path
from instagram import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpost', views.NewPost, name='newpost'),
    path('<uuid:post_id>/like', views.like, name='like'),
    

]

