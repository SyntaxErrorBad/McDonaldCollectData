from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from ScrapingApi.scraping.scraping_load_json import load_data_from_json_file
from ScrapingApi.scraping.scraping_data import write_scraping_data


class StartScrapingAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            write_scraping_data()
            return Response({"message": "scraping finished"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "something wrong, try again, maybe lets admin check url"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AllProductsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        product_json_data = load_data_from_json_file()
        return Response(product_json_data, status=status.HTTP_200_OK)


class ProductByNameAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_name):
        product_json_data = load_data_from_json_file()[product_name]
        return Response(product_json_data, status = status.HTTP_200_OK)


class ProductByNameFieldAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_name, product_field):
        product_json_data = load_data_from_json_file()[product_name]
        if product_field == "description":
            response = product_json_data[product_field]
        else:
            response = product_json_data['nutrient_facts'][product_field]
        return Response(response, status=status.HTTP_200_OK)
