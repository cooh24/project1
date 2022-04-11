from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from .models import Post, Category, Tag
from django.core.exceptions import PermissionDenied

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

# post 생성 페이지 클래스 생성
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()

                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')

                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)
            return response
        else:
            return redirect('/classnote/')

# post 업데이트 페이지 클래스 생성
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category',]

    template_name = 'classnote/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = '; '.join(tags_str_list)
        return context

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        # 수정을 위한 PostUpdate 객체의 데이터에서 tags 속성의 값을 저장해놓은 것을 제거하기 위함 -> 새로 입력된 tags 값을 다시 추가를 하기 때문에
        self.object.tags.clear()

#카테고리 페이지를 만드는 함수생성
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(request, 'classnote/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )

#Tag 페이지를 만드는 함수생성
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(request, 'classnote/post_list.html',
        {
            'post_list' : post_list,
            'tag' : tag,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
        }
    )