from django_filters import FilterSet, CharFilter
from .models import Comment


class CommentFilter(FilterSet):
    advertisement__title__icontains = CharFilter(label='Заголовок объявления')

    class Meta:
        model = Comment
        fields = {
            'advertisement__title': ['icontains'],
        }