# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

# Create your views here.

# Postlist를 ListView로 클래스생성 / index함수 대체
class PostList(ListView):
    model = Post
    ordering = '-pk'
    
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    # template_name = 'classnote/index.html'    # 직접 지정
    # ListView는 모델명뒤에 '_list'가 붙는 html파일을 기본템플릿으로 사용 / Post모델 : post_list

# index 화면에 포스트모델의 객체를 최근생성순으로 불러오도록 함수생성
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(request, 'classnote/index.html', {'posts':posts,})



# post 상세페이지를 DetailView로 클래스생성 / single_post_page 함수 대체
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    
# single_post_page에 id=pk 값에 해당하는 포스트를 불러오는 함수 생성
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'classnote/single_post_page.html', {'post':post,})