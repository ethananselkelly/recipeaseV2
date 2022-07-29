from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Recipe(Model):
  id = fields.IntField(pk=True)
  url = fields.TextField(null=True, unique=True)
  title = fields.TextField()
  image = fields.TextField(null=True)
  host = fields.TextField(null=True)
  total_time = fields.IntField(null=True)
  ingredients = fields.JSONField()
  instructions = fields.TextField()
  notes = fields.TextField(null=True)
  created = fields.DatetimeField(auto_now_add=True)
  updated = fields.DatetimeField(auto_now=True)

  # RELATIONAL FIELDS
  tags = fields.ManyToManyField('models.Tag', related_name='recipes', through='recipe-tags')
  users = fields.ManyToManyField('models.User', related_name='users', through='recipe-users')

  class Meta:
    table = 'recipes'

Recipe_Pydantic = pydantic_model_creator(Recipe, name='Recipe')
RecipeIn_Pydantic = pydantic_model_creator(Recipe, name='RecipeIn', exclude_readonly=True)