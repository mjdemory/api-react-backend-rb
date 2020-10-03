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
        post = self.get_object()
        post.upvote = post.upvote + 1
        post.vote_score = post.vote_score +1
        post.save()
        return Response({'status': 'upvote success'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvote = post.downvote - 1
        post.vote_score = post.vote_score - 1
        post.save()
        return Response({'status': 'downvote success'})

    @action(detail=False)
    def VoteScoreViewSet(self, request):
        boast = RoastBoastModel.objects.order_by('vote_score')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)
