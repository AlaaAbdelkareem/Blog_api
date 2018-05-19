from rest_framework import serializers

from blog.models import Posts

from blog.models import Comments


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__' #('post')

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__' #('post')
