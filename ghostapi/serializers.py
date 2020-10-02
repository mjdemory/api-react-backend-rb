from rest_framework.serializers import ModelSerializer, StringRelatedField

from ghostapi.models import RoastBoastModel

class RoastBoastSerializer(ModelSerializer):
    class Meta:
        model = RoastBoastModel
        fields = [
            'id',
            'body',
            'choices',
            'upvote',
            'downvote',
            'vote_score',
            'post_date'
        ]