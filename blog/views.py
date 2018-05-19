from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Posts,Comments
from blog.serializers import PostsSerializer,CommentsSerializer



@api_view(['GET', 'POST'])
def posts_list(request):
    """
    List all postss, or create a new posts.
    """
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    """
    Get, udpate, or delete a specific posts
    """
    try:
        posts = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostsSerializer(posts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostsSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def comments_list(request):
    """
    List all commentss, or create a new comments.
    """
    if request.method == 'GET':
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def comments_detail(request, pk):
    """
    Get, udpate, or delete a specific comments
    """
    try:
        comments = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentsSerializer(comments)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentsSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)