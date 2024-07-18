import logging.config
from rest_framework.views import APIView
from rest_framework.response import Response


log = logging.getLogger(__name__)


class OrdersValidationView(APIView):
    def post(self, request, *args, **kwargs):





        return Response({'message': 'success', "payload": []}, status=200)