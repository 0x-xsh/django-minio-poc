from minio import Minio, S3Error
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadView(APIView):

    def post(self, request):

        try:
            file = request.data['file']

        except:
            return Response({"error": "no file"})

        minio_client = Minio("127.0.0.1:9000",
                             access_key="minioadmin",
                             secret_key="minioadmin",
                             secure=False)


        try:
            minio_client.make_bucket("files")

        except S3Error as err:
           Response({"error": str(err)})


        try:
            minio_client.put_object("files", file.name, file, file.size)
            # sync?

        except S3Error as err:
            return Response({"error": str(err)})

        return Response({"message": "File uploaded successfully"})
