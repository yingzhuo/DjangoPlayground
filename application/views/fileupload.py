r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django.core.files import storage
from rest_framework import views, parsers
from rest_framework.response import Response

from application.views.fileupload_form import CommonFileUploadForm


class FileUploadView(views.APIView):
    parser_classes = [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        form = CommonFileUploadForm(data=request.data)
        form.is_valid(raise_exception=True)

        filename = form.validated_data['filename']
        file = form.validated_data['file_data']

        fs = storage.FileSystemStorage()
        save_file_name = fs.save(filename, file)

        print(save_file_name)

        return Response()
