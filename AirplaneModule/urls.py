from django.urls import path

from AirplaneModule.views import index,detail_view,delete,add_new

urlpatterns = [
    path('add/', name='airplane add', view=add_new),
    path('delete/<int:id>', name='airplane delete', view=delete),
    path('view/<int:id>', name='airplane detailview', view=detail_view),
    path('', name='airplane listview', view=index),
]