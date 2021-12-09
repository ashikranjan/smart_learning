import boto3
import os
from django.conf import settings
from werkzeug.utils import secure_filename
from django.core.files.storage import FileSystemStorage


class AWSManager:
    def __init__(self, aws_access_key=settings.AWS_ACCESS_KEY_ID, aws_secret_key=settings.AWS_SECRET_ACCESS_KEY):
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key

    def upload_file_to_s3(self, file, folder="public"):
        filename = ""
        try:
            filename = secure_filename(file.name)
            fs = FileSystemStorage()
            filename = fs.save(filename, file)
            s3 = boto3.client(
                "s3",
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key,
            )
          
            file_path = filename
            if folder != "":
                file_path = folder + "/" + filename

            s3.upload_file(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Filename=filename,
                Key=file_path,
                ExtraArgs={"ACL": "public-read"},
            )
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
            except Exception as e:
                pass

            return filename
        except Exception as e:
            return False