from django.urls import path

from FlightModule.views import index,detail_view,delete,add_new

urlpatterns = [
    path('add/', name='flight add', view=add_new),
    path('delete/<int:id>', name='flight delete', view=delete),
    path('view/<int:id>', name='flight detailview', view=detail_view),
    path('', name='flight listview', view=index),
]