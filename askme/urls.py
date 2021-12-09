from askme.views import (
    SubmitQueryView,
    UploadQueryDocumentView, 
    AnswerQueryView
    )
from django.urls import path

urlpatterns = [
    path('ask/query', SubmitQueryView.as_view()),
    path('query/<int:query_id>/document', UploadQueryDocumentView.as_view()),
    path('reply/query/<int:query_id>', AnswerQueryView.as_view())
]
