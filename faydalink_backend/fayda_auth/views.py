from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class FaydaLogin(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token required"}, status=400)
        user = authenticate(request, token=token)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Authentication failed"}, status=401)

class CustomerSearch(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        fin = request.data.get('fin')
        if not fin:
            return Response({"error": "FIN required"}, status=400)
        # Mock response - replace with actual Fayda API call
        return Response({
            "fin": fin,
            "name": "Meron Alemayehu",
            "credit_score": 750,
            "national_id": "ET-NID-123456789",
            "photo_url": "/media/nid_photos/123456789.jpg"
        })
