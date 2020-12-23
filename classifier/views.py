from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from bloxplorer import bitcoin_testnet_explorer as test_explorer
from bloxplorer import bitcoin_explorer as explorer
from .bitcoin import *
from .bitcoin import get_opcodes_from_string
import json


# Create your views here.


class TestTransactionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            return Response(test_explorer.tx.get(kwargs['tx']).data)
        except:
            raise Http404


class TransactionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            return Response(explorer.tx.get(kwargs['tx']).data)
        except:
            raise Http404


class TransactionScriptView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            trans = Transaction(explorer.tx.get(kwargs['tx']))
            return Response(json.loads(json.dumps(trans, cls=DefaultEncoder)))
        except:
            raise Http404


class TestTransactionScriptView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            trans = Transaction(test_explorer.tx.get(kwargs['tx']))
            return Response(json.loads(json.dumps(trans, cls=DefaultEncoder)))
        except:
            raise Http404


class TransactionValidationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            temp = explorer.tx.get(kwargs['tx']).data
            return Response(status=200)
        except:
            raise Http404


class TestTransactionValidationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            temp = test_explorer.tx.get(kwargs['tx']).data
            return Response(status=200)
        except:
            raise Http404


class ScriptVisualisationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            script = request.data.get("script")
            res = ScriptInterpreter(get_opcodes_from_string(script)).execute()
            return Response(data=json.loads(json.dumps(res, cls=DefaultEncoder)))
        except:
            raise Http404


class OpcodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            script = request.data.get("script")
            res = get_opcodes_from_string(script)
            return Response(data=json.loads(json.dumps(res, cls=DefaultEncoder)))
        except:
            raise Http404