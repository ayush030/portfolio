from django.urls import path
from .views import IntroductionView

urlpatterns = [
    # CRUD for Introduction(s)
    path("", IntroductionView.as_view(), name="introduction")
]
