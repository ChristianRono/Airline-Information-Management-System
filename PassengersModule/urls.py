from django.urls import path

from PassengersModule.views import index,detail_view,delete,add_new

urlpatterns = [
    path('add/', name='passenger add', view=add_new),
    path('delete/<int:id>', name='passenger delete', view=delete),
    path('view/<int:id>', name='passenger detailview', view=detail_view),
    path('', name='passenger listview', view=index),
]