from django.urls import path

from StaffModule.views import index,detail_view,delete,add_new

urlpatterns = [
    path('add/', name='staff add', view=add_new),
    path('delete/<int:id>', name='staff delete', view=delete),
    path('view/<int:id>', name='staff detailview', view=detail_view),
    path('', name='staff listview', view=index),
]