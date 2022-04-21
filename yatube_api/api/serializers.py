from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import (
    Post,
    Group,
    Comment,
    User,
    Follow
)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, default=serializers.CurrentUserDefault(),
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, default=serializers.CurrentUserDefault(),
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    def validate_following(self, value):

        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Попытка подписаться на самого себя')
        return value

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
