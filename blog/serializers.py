from rest_framework import serializers
from .models import Comments, Likes, PostList


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            "id",
            "post",
            "user",
            "body",
            "created",
            "updated",
        )

    def create(self, validated_data):
        comment = Comments.objects.create(**validated_data)
        comment.save()
        return comment
    
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = (
            "id",
            "post",
            "name",
            "created",            
        )

    def create(self, validated_data):
        likes = Likes.objects.create(**validated_data)
        likes.save()
        return likes


class PostListSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_comments(self, obj):
        serializer = CommentSerializer(obj.comment, many=True)
        return(serializer.data)

    def get_comments_count(self, obj):
        return obj.comment.count()

    def get_likes_count(self, obj):
        return obj.like.count()

    class Meta:
        model = PostList
        fields = (
            "id",
            "title",
            "category",
            "content",
            "image",
            "status",
            "published_date",
            "author",
            "comments",
            "comments_count",
            "likes_count",
        )


# class PostDetailSerializer(serializers.ModelSerializer):
#     comments = serializers.SerializerMethodField()
#     comments_count = serializers.SerializerMethodField()
#     likes_count = serializers.SerializerMethodField()

#     def get_comments(self, obj):
#         serializer = CommentSerializer(obj.comment, many=True)
#         return(serializer.data)

#     def get_comments_count(self, obj):
#         return obj.comment.count()

#     def get_likes_count(self, obj):
#         return obj.like.count()

#     class Meta:
#         model = PostList
#         fields = (
#             "id",
#             "title",
#             "category",
#             "content",
#             "image",
#             "status",
#             "published_date",
#             "author",
#             "comments",
#             "comments_count",
#             "likes_count",
#         )
