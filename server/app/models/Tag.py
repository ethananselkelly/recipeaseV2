from tortoise.models import Model
from tortoise import fields

from server.app.models.Recipe import Recipe

class Tag(Model):
  id = fields.IntField(pk=True)
  tag = fields.CharField(max_length=50, null=False)

  class Meta:
    table = 'tag'