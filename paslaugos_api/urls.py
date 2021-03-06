from .views import (
    PostList,
    PostListSearch,
    UserPostDetails,
    CreatePost,
    DeletePost,
    UpdatePost,
    UserOrders,
    OrdersFromUser,
    PostReview,
    CreateOrder,
    UpdateOrder,
)
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = "paslaugos_api"

router = DefaultRouter()
router.register("post", PostList, basename="post")
##router.register("search", PostListSearch, basename="Post Search")


urlpatterns = [
    path("search/", PostListSearch().as_view(), name="postSearch"),
    ## User customization views
    path("admin/<int:pk>/", UserPostDetails().as_view(), name="adminView"),
    path("admin/create", CreatePost().as_view(), name="createPost"),
    path("admin/delete/<int:pk>", DeletePost().as_view(), name="deletePost"),
    path("admin/edit/<int:pk>", UpdatePost().as_view(), name="updatePost"),
    ## User orders
    path("admin/order/buy/<int:pk>/", UserOrders().as_view(), name="orderBuyerView"),
    path(
        "admin/order/sell/<int:pk>/", OrdersFromUser().as_view(), name="orderSellerView"
    ),
    path("admin/order/update/<int:pk>", UpdateOrder().as_view(), name="UpdateOrder"),
    path("admin/order/create", CreateOrder().as_view(), name="createOrder"),
    ## User reviews
    path("review/<int:pk>/", PostReview().as_view(), name="postReview"),
]


urlpatterns += router.urls
