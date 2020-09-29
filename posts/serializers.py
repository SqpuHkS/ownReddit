from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'user', 'user_id', 'created']

class VoteSerializer(serializers.ModelSerializer):
   class Meta:
        model = Vote
        fields = ['id']