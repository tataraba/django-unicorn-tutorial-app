from django.db import models


class Meal(models.Model):
    TYPE_OF_MEAL = {
        "B": "Breakfast",
        "L": "Lunch",
        "D": "Dinner",
        "S": "Snack",
    }
    name = models.CharField(max_length=100)
    main_dish = models.CharField(max_length=50)
    side_dish = models.CharField(max_length=50, blank=True)
    desert = models.CharField(max_length=50, blank=True)
    type_of_meal = models.CharField(max_length=1, choices=TYPE_OF_MEAL.items(), blank=True)

    def __str__(self):
        return self.name