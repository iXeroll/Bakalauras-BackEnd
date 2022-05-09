from rest_framework import serializers
from paslaugos.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "description",
            "image",
            "status",
            "price",
            "creationDate",
            "updateDate",
        )
