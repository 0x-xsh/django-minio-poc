import json
from datetime import timedelta

from django.http import HttpResponse
from minio import Minio, S3Error

from rest_framework.views import APIView


class SignedUrlView(APIView):

    def get(self, request):

        minio_client = Minio("127.0.0.1:9000",
                             access_key="minioadmin",
                             secret_key="minioadmin",
                             secure=False)
        try:
            objects = [x.object_name for x in minio_client.list_objects("files")]
        except:
            return HttpResponse("error")

        if len(objects) == 0:
            return HttpResponse("no objects")

        to_be_signed = objects[0]

        try:
            url = minio_client.presigned_get_object(bucket_name='files',
                                                    object_name=to_be_signed,
                                                    expires=timedelta(seconds=11.0))


        except S3Error as err:
            return HttpResponse(str(err))

        return HttpResponse(url)
