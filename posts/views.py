from .serializers import PostSerializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
