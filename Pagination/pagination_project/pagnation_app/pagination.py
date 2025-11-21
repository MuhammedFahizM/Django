from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'p'
    max_page_size = 10

