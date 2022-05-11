from rest_framework import serializers
from paslaugos.models import Post, Order


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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "buyer",
            "seller",
            "post",
            "comment",
            "status",
            "price",
            "creationDate",
            "completionDate",
        )
