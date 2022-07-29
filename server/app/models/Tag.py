from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from server.app.models.Recipe import Recipe

class Tag(Model):
  id = fields.IntField(pk=True)
  tag = fields.CharField(max_length=50, null=False)
  recipes : fields.ManyToManyRelation[Recipe]

  class Meta:
    table = 'tags'

Tag_Pydantic = pydantic_model_creator(Tag, name='Tag')
TagIn_Pydantic = pydantic_model_creator(Tag, name='TagIn', exclude_readonly=True)