from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase
class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_is_not_recipe_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':2}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templates_loads_recipes(self):
        self.make_recipe()
        response =self.client.get(reverse('recipes:category',args=(1,)))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
 
        self.assertIn('Título da Receita', content)

    def test_recipe_category_templates_dont_loads_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':recipe.category.id}))
        self.assertEqual(response.status_code, 404)
