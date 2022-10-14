from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000 과 views.py 폴더의 index 함수 연결
    path('post/', views.post, name='post'), # 127.0.0.1:8000/post 과 views.py 폴더의 post 함수 연결
    path('post/delete/<int:id>', views.delete_post, name='delete-post'),
    path('post/update/<int:id>', views.update_post, name='update-post'),

]
