from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ShelfLayoutSerializer
from .services import ShapeDetector


class AnalyzeShelfView(APIView):

    def post(self, request):

        serializer = ShelfLayoutSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            layout = serializer.validated_data["layout"]

            result = ShapeDetector.analyze(layout)

            return Response(
                {"success": True, "data": result}, status=status.HTTP_200_OK
            )

        except ValueError as e:

            return Response(
                {"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

        except Exception:

            return Response(
                {"success": False, "error": "Internal server error."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
