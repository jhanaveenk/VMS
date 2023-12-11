from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorsSerializer
from .models import Vendors


class VendorsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Vendors.objects.all().order_by('id')
        serializer = VendorsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = VendorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f"Serializer Errors: {serializer.errors}")
        return Response(status=status.HTTP_400_BAD_REQUEST)