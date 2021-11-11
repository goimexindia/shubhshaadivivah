import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    city = CharFilter(field_name='city', lookup_expr='icontains')
    start_age = CharFilter(field_name="age", lookup_expr='gte')
    end_age = CharFilter(field_name="age", lookup_expr='lte')
    user_id = CharFilter(field_name="id", lookup_expr='iexact')

    class Meta:
        model = Profile
        fields = ('languages', 'caste', 'religion', 'education', 'state',)

        exclude = ['email',
                   'birthday', 'birthtimehh', 'birthtimemm', 'birthplace', 'birthstate', 'birthcountry', 'ampm',
                   'email_confirmed',
                   'mobile_confirmed',
                   'mobile',
                   'address ',
                   'number',
                   'website',
                   'view_count', 'img', 'videofile', 'img1', 'img2', 'img3', 'img4',
                   'created_at']
