from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ghostapi.serializers import RoastBoastSerializer
from ghostapi.models import RoastBoastModel

# Create your views here.

class RoastBoastViewSets(viewsets.ModelViewSet):
    queryset = RoastBoastModel.objects.all()
    serializer_class = RoastBoastSerializer

    @action(detail=False)
    def BoastViewSet(self, request):
        boast = RoastBoastModel.objects.filter(choices=True).order_by('post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def RoastViewSet(self, request):
        roast = RoastBoastModel.objects.filter(choices=False).order_by('post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = RoastBoastModel.objects.get(id=pk)
        serializer = RoastBoastSerializer(data=request.data)
        if serializer.is_valid():
            post.upvote = post.upvote + 1
            post.vote_score = post.vote_score +1
            post.save()
            return Response({'status': 'upvote added'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = RoastBoastModel.objects.get(id=pk)
        serializer = RoastBoastSerializer(data=request.data)
        if serializer.is_valid():
            post.downvote = post.downvote - 1
            post.vote_score = post.vote_score - 1
            post.save()
            return Response({'status': 'downvote added'})

    @action(detail=True, methods=['post'])
    def create_post(self, request, pk=None):
        post = self.get_object()
        serializer = RoastBoastSerializer(data=request.data)
        if serializer.is_valid():
            post.create_post(serializer.data['body', 'choices'])
            post.save()
            return Response({'status': 'post created'})
