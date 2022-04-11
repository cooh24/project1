from django.urls import path
from . import views

urlpatterns = [

    path('<int:pk>/', views.PostDetail.as_view()),  #PostDetail 경로
    # path('<int:pk>/', views.single_post_page),

    path('', views.PostList.as_view()),  #views에 정의된 PostList를 view로 보여주는 경로
    # path('', views.index),
]