from django.conf.urls import url

from .views import ReaderCreation, ReaderDelete, ReaderList, ReaderUpdate, ReaderDetail

app_name='readers'
urlpatterns = [
    url(r'^$', ReaderList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ReaderDetail.as_view(), name='detail'),
    url(r'^nuevo$', ReaderCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ReaderUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ReaderDelete.as_view(), name='delete'),
]