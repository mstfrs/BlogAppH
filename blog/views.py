from .models import Comments, Likes, PostList
from .serializers import PostListSerializer, CommentSerializer,LikeSerializer
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView 

class PostCreate(ListCreateAPIView):
    queryset = PostList.objects.all()
    serializer_class = PostListSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = PostList.objects.all()
    serializer_class = PostListSerializer
    
    
class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    
class LikeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
