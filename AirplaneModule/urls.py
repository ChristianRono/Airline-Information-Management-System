from django.urls import path

from AirplaneModule.views import AirplaneListView,AirplaneDetailView,delete

urlpatterns = [
    path('delete/<int:id>', name='airplane delete', view=delete),
    path('view/<int:pk>', name='airplane detailview', view=AirplaneDetailView.as_view()),
    path('', name='airplane listview', view=AirplaneListView.as_view()),
]