from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response

from authAppExample.models.product                    import Product
from authAppExample.serializers.productSerializer     import ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductCreateView(generics.CreateAPIView):
    serializer_class   = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response("TODO BIEN", status = status.HTTP_201_CREATED)


class ProductUpdateView(generics.UpdateAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ProductDeleteView(generics.DestroyAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)