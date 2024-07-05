from django.core.paginator import Paginator
from django.shortcuts import render
from habits.models import Habit


def habit_list(request):
    # Get the list of habits
    habits = Habit.objects.all()

    # Set the number of habits to display per page
    habits_per_page = 5

    # Create a paginator object
    paginator = Paginator(habits, habits_per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page', 1)

    # Get the habits for the current page
    habits_page = paginator.get_page(page_number)

    # Render the habit list template with the habits and pagination information
    return render(request, 'habits/habit_list.html', {'habits': habits_page})