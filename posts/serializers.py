from rest_framework import serializers
from .models import Post, vote

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','title','url','poster','poster_id','created','votes']

    def get_votes(self, post):
        return vote.objects.filter(post=post).count()
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = vote
        fields = ['id']