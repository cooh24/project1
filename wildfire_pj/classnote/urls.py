from django.urls import path
from . import views

urlpatterns = [
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),

    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),

    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),

    path('<int:pk>/', views.PostDetail.as_view()),  #PostDetail 경로
    # path('<int:pk>/', views.single_post_page),
    path('', views.PostList.as_view()),  #views에 정의된 PostList를 view로 보여주는 경로
    # path('', views.index),
]