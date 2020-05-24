from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = {
    path('create-bucket', views.CreateView.as_view(), name="create"),
    path('list-bucket', views.CreateView.as_view(), name='list'),
    path('details-bucket/<int:pk>', views.DetailsView.as_view(), name="details-bucket")
}

urlpatterns = format_suffix_patterns(urlpatterns)