from django.test import TestCase
from recipes.models import Category,Recipe,User

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp() 
    
    def make_category (self,name='categoria'):
       return Category.objects.create(name='categoria')

    def make_author(
            self,
            username="name",
            password="123456",
            first_name="user",
            last_name = "last",
            email="user@email.com",):

        return User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name = last_name,
            email=email,
            )
    
    def make_recipe(
            self,            
            title='Título da Receita',
            description='Descrição simples',
            slug='titulo-da-receita',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Etapas de preparo',
            is_published=True,
            category_data=None,
            author_data=None,):
        
        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data={}
        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            is_published=is_published,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )

