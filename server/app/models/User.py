from msilib.schema import Class
from tortoise.models import Model
from tortoise import fields

class User(Model):
  id = fields.IntField(pk=True)
  username = fields.CharField(max_length=50)
  email = fields.TextField()
  hashed_password = fields.TextField()
  created_at = fields.DatetimeField(null=True, auto_now=True)
  updated_at = fields.DatetimeField(null=True, auto_now=True)

  class Meta:
    table = "user"