from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from server.app.models.Recipe import Recipe

class User(Model):
  id = fields.IntField(pk=True)
  email = fields.TextField()
  hashed_password = fields.TextField()
  created_at = fields.DatetimeField(null=True, auto_now=True)
  updated_at = fields.DatetimeField(null=True, auto_now=True)
  recipes: fields.ManyToManyRelation[Recipe]

  class Meta:
    table = "users"

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)