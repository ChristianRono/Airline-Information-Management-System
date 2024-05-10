from django.urls import path

from CitiesModule.views import index,detail_view,delete,add_new

urlpatterns = [
    path('add/', name='city add', view=add_new),
    path('delete/<int:id>', name='city delete', view=delete),
    path('view/<int:id>', name='city detailview', view=detail_view),
    path('', name='city listview', view=index),
]