from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class MyApis(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=True)
    description = fields.CharField(max_length=200, null=True)
    polling_frequency = fields.IntField()
    polling_unit = fields.CharField(max_length=12, null=True) #seconds/minute
    url = fields.CharField(max_length=100, null=True)
    http_headers = fields.CharField(max_length=100, null=True)
    query_params = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

MyApiPydantic = pydantic_model_creator(MyApis, name="MyApi")
MyApisInPydantic = pydantic_model_creator(MyApis, name="MyApiIn", exclude_readonly=True)


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    full_name = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=50, null=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    #class PydanticMeta:
    #    exclude = ["password"]


UserPydantic = pydantic_model_creator(Users, name="User", exclude=("email", "hashed_password"))
UserInPydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)