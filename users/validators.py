from rest_framework import status
from rest_framework.exceptions import ValidationError




class Validate:
    @classmethod
    def is_valiadate(cls, **fields):
        for filed in fields:
            if not fields.get(filed):
                raise ValidationError({"message": f"{filed} is missing", "status": False})
            