from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('auth', include('rest_framework.urls'), name="rest_framework"),
    path('create-bucket', views.CreateView.as_view(), name="create"),
    path('list-bucket', views.CreateView.as_view(), name='list'),
    path('details-bucket/<int:pk>', views.DetailsView.as_view(), name="details-bucket"),
    path('get-token', obtain_auth_token)

}

urlpatterns = format_suffix_patterns(urlpatterns)