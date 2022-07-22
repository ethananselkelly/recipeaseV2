from tortoise.models import Model
from tortoise import fields

class Recipe(Model):
  id = fields.IntField(pk=True)
  url = fields.TextField(null=True)
  title = fields.TextField()
  image = fields.TextField(null=True)
  host = fields.TextField(null=True)
  total_time = fields.IntField(null=True)
  ingredients = fields.JSONField()
  instructions = fields.TextField()
  notes = fields.TextField()
  created = fields.DatetimeField(auto_now_add=True)

  # FIGURE OUT MANY TO MANY FIELDS ARGH
  tags = fields.ManyToManyField('models.Tag', related_name='recipe', through='recipe-tag')
  users = fields.ManyToManyField('models.User', related_name='user', through='recipe-user')

  class Meta:
    table = 'recipe'