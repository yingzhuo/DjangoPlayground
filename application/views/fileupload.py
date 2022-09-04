r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django_sugar import web
from rest_framework import views, parsers
from rest_framework.response import Response

from application.views.fileupload_form import CommonFileUploadForm

# 文件存储
FILE_STORAGE = web.SmartFileSystemFileStorage()


class FileUploadView(views.APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        form = CommonFileUploadForm(data=request.data)
        form.is_valid(raise_exception=True)

        filename = form.validated_data['filename']
        file = form.validated_data['file_data']

        path = FILE_STORAGE.save(filename, file)

        return Response({
            'path': path
        })
