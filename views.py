from django.shortcuts import render
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from.models import Truth
from.serializers import TruthSerializers

class StudentCurd(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        if pk:
            student = get_object_or_404(Truth, id=pk)
            student_serializers = TruthSerializers(student)
            return Response(student_serializers.data, status=status.HTTP_200_OK)
        else:
            students_qs = Truth.objects.all()
            student_serializers = TruthSerializers(students_qs, many=True)
            return Response(student_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_serializers = TruthSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        student = get_object_or_404(Truth, id=pk)
        student_serializers = TruthSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, format=None):
        student = get_object_or_404(Truth, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)