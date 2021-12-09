from rest_framework.response import Response
from rest_framework import status


class APIResponse(Response):
    def __init__(self, data={}, status=status.HTTP_200_OK, message="Success"):
        result = {'data': data, 'message': message, "status": status}
        super(APIResponse, self).__init__(data=result, status=status)

