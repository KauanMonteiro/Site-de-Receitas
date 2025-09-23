from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase
class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_page_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe',kwargs={'id':1}))
        self.assertIs(view.func, views.recipe)
        
    def test_recipe_detail_page_view_returns_404_is_not_recipe_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':2}))
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_detail_templates_loads_the_correct_recipes(self):
        self.make_recipe()
        response =self.client.get(reverse('recipes:recipe',kwargs={'id':1}))
        content = response.content.decode('utf-8')
 
        self.assertIn('Título da Receita', content)  

    def test_recipe_detail_templates_dont_loads_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response =self.client.get(reverse('recipes:recipe',kwargs={'id':recipe.id}))
        self.assertEqual(response.status_code, 404)
