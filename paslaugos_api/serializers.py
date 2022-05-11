from rest_framework import serializers
from paslaugos.models import Post, Order, Review


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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "post", "author", "title", "comment", "creationDate")
