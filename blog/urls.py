from django.urls import path, include
from .views import PostList, PostDetail, PostCreate,CommentDetail,LikeDetail


urlpatterns = [


    path('list/', PostCreate.as_view(), name="postlist"),
    path('list/<int:pk>/', PostDetail.as_view(), name="postdetail"),
    path('list/<int:pk>/comment/', CommentDetail.as_view(), name="commentdetail"),
    path('list/<int:pk>/like/', LikeDetail.as_view(), name="likedetail"),

]
