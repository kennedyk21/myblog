from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blog/<int:post_id>/', views.post_page, name='post_page'),
    path('blog/suggestion/',views.suggestion_view, name='suggestion'),
    path('blog/<int:post_id>/comment/',views.comments, name='comment'),
]