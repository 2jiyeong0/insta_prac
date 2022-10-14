from django.contrib.auth.decorators import login_required
from matplotlib.style import context
from .models import Post
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/post')
    else:
        return redirect('/account/signin')


def post(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
        if user:    # 로그인 한 사용자
            all_post = Post.objects.all().order_by('-created_at')
            return render(request, 'post/index.html', {'post': all_post})
        else:
            return redirect('/account/signin')

    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_post = Post()  # 글쓰기 모델 가져오기
        my_post.author = user  # 모델에 사용자 저장
        my_post.content = request.POST.get('my-content', '')  # 모델에 글 저장
        my_post.save()
        return redirect('/post')

# 게시글 삭제
@login_required
def delete_post(request, id):
    my_post = Post.objects.get(id=id)
    my_post.delete()
    return redirect('/post')

@login_required
def update_post(request, id):
    my_post = Post.objects.get(id=id)

    if request.method == "POST":
        my_post.content = request.POST['content']
        my_post.author = request.POST['author']

        post.save()
        return redirect('/post')

    else:
        postForm = Post
        return render(request, 'update.html', {'postForm':postForm})