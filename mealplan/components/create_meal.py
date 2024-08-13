from django_unicorn.components import UnicornView

from mealplan.forms import MealForm
from mealplan.models import Meal


class CreateMealView(UnicornView):
    state: str = "Add"
    meals: list[Meal] = None

    form_class = MealForm
    name = None
    main_dish = None
    side_dish = None
    desert = None
    type_of_meal = None

    def mount(self):
        self.meals = Meal.objects.all()

    def add(self):
        self.reset()
        self.name = None
        self.main_dish = None
        self.side_dish = None
        self.desert = None
        self.type_of_meal = None
        self.state = "Cancel"

    def cancel(self):
        self.reset()
        self.state = "Add"

    def create(self):
        if not self.is_valid():
            return

        _new_meal = Meal.objects.create(
            name=self.name,
            main_dish=self.main_dish,
            side_dish=self.side_dish,
            desert=self.desert,
            type_of_meal=self.type_of_meal
        )

        self.meals = Meal.objects.all()
        self.state = "Add"

    def clear(self):
        _remove_all_meals = Meal.objects.all().delete()
        self.mount()