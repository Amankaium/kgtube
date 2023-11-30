import django_filters
from .models import Video


class VideoFilter(django_filters.FilterSet):
    likes_from = django_filters.NumberFilter(
        field_name="likes",
        lookup_expr="gte",
        label="Лайков больше чем"
    )
    likes_to = django_filters.NumberFilter(
        field_name="likes",
        lookup_expr="lte",
        label="Лайков меньше чем"
    ) 

    class Meta:
        model = Video
        fields = ['author']
