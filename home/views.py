from rest_framework.views import APIView
from .models import Introduction
from .serializers import IntroductionSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


class IntroductionView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # Get introduction
    def get(self, request, *args, **kwargs):
        intro = Introduction.objects.all()
        serialized_object = IntroductionSerializer(intro, many=True)

        return Response(serialized_object.data, status=status.HTTP_200_OK)

    # Create introduction
    def post(self, request, *args, **kwargs):
        intro_count = Introduction.objects.count()

        if intro_count > 0:
            intro_exist_error = "Introduction already exists, try updating it or delete existing one."
            return JsonResponse(
                data={
                        "error": intro_exist_error
                },
                status=status.HTTP_409_CONFLICT
            )

        payload = JSONParser().parse(request)

        serializer = IntroductionSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete introduction
    def delete(self, request):
        """ since only one introduction is allowed, delete it once receive the request """

        intro_count = Introduction.objects.count()

        if intro_count == 0:
            return JsonResponse(
                data={
                    "error" : "no Introduction found."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        intro = Introduction.objects.all()
        serialized_object = IntroductionSerializer(intro, many=True)

        intro.delete()

        return JsonResponse(
            data={
                "object": serialized_object.data
            },
            status=status.HTTP_204_NO_CONTENT
        )
