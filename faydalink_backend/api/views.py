from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Customer

class CustomerSearch(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        fin = request.data.get('fin')
        if not fin:
            return Response({"error": "FIN required"}, status=400)
        try:
            customer = Customer.objects.get(fin=fin)
            return Response({
                "name": customer.name,
                "fin": customer.fin,
                "credit_score": customer.credit_score,
                "credit_limit": customer.credit_limit,
                "national_id_data": self.get_national_id_data(fin)
            })
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)

    def get_national_id_data(self, fin):
        # In real implementation, call Fayda API with staff credentials
        # This is a mock response
        return {
            "full_name": "Meron Alemayehu",
            "dob": "1985-07-15",
            "photo_url": "https://example.com/photos/meron.jpg"
        }
