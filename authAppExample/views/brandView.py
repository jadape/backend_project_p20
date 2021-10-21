from django.conf                                import settings
from rest_framework                             import generics, status
from rest_framework.response                    import Response

from authAppExample.models.brand                import Brand
from authAppExample.serializers.brandSerializer import BrandSerializer


class BrandCreateView(generics.CreateAPIView):
    serializer_class = BrandSerializer

    def post(self, request, *args, **kwargs):
        serializer = BrandSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response("TODO BIEN", status = status.HTTP_201_CREATED)


class BrandUpdateView(generics.UpdateAPIView):
    queryset           = Brand.objects.all()
    serializer_class   = BrandSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class BrandDeleteView(generics.DestroyAPIView):
    queryset           = Brand.objects.all()
    serializer_class   = BrandSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BrandDetailView(generics.RetrieveAPIView):
    queryset           = Brand.objects.all()
    serializer_class   = BrandSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
