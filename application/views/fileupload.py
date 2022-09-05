r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django.utils import timezone
from rest_framework import views, parsers
from rest_framework.response import Response

from application.models import FileMeta, FileMetaSerializer
from application.views.fileupload_form import CommonFileUploadForm
from common import constants, security


class FileUploadView(views.APIView):
    parser_classes = [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        current_user_id = security.get_current_user_id(request)

        form = CommonFileUploadForm(data=request.data)
        form.is_valid(raise_exception=True)

        fs = constants.DEFAULT_FILE_STORAGE
        filename = form.validated_data['filename']
        file = form.validated_data['file_data']

        # 文件保存到本地
        path = fs.save(filename, file)

        filemeta = FileMeta()
        filemeta.path = path
        filemeta.created_date = timezone.now()
        filemeta.created_user_id = current_user_id
        filemeta.save()

        ser = FileMetaSerializer(instance=filemeta, many=False)
        return Response(data=ser.data)
