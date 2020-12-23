from django.urls import path
from .views import TransactionView, TestTransactionView, TransactionScriptView, TestTransactionScriptView, TestTransactionValidationView, TransactionValidationView, ScriptVisualisationView, OpcodeView

app_name = "classifier"

urlpatterns = [
    path('transaction/<str:tx>/script', TransactionScriptView.as_view()),
    path('transaction/<str:tx>/valid', TransactionValidationView.as_view()),
    path('transaction/<str:tx>', TransactionView.as_view()),
    path('transaction/test/<str:tx>/script', TestTransactionScriptView.as_view()),
    path('transaction/test/<str:tx>/valid', TestTransactionValidationView.as_view()),
    path('transaction/test/<str:tx>', TestTransactionView.as_view()),
    path('visualize_script', ScriptVisualisationView.as_view()),
    path('opcodes', OpcodeView.as_view())
]