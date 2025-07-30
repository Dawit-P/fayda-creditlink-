from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .verifayda_oidc import get_user_info

# Create your views here.

@api_view(['GET'])
def verify_fin(request):
    fin = request.query_params.get('fin')
    if not fin:
        return Response({'error': 'Missing fin parameter'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_info = get_user_info(fin)
        return Response(user_info, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
