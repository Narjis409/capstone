from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Meals
from .forms import MealsForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin



class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff 

  
class MealsListView(StaffRequiredMixin,ListView):
    model = Meals
    template_name = 'meals_list.html' 
    

    def get_queryset(self):
        return Meals.objects.filter(available=True)
    


class MealsDetailView(StaffRequiredMixin, DetailView):
    model = Meals
    template_name = 'meals_detail.html'  
    context_object_name = 'meal'


class MealsCreateView(StaffRequiredMixin, CreateView):
    model = Meals
    form_class = MealsForm
    template_name = 'meals_form.html' 
    success_url = reverse_lazy('meals_list')

    def form_valid(self, form):
        messages.success(self.request, "Meal has been successfully added!")
        return super().form_valid(form)


class MealsUpdateView(StaffRequiredMixin, UpdateView):
    model = Meals
    form_class = MealsForm
    template_name = 'meals_form.html'  
    success_url = reverse_lazy('meals_list')


    def form_valid(self, form):
        messages.success(self.request, "Meal has been successfully dupdated!")
        return super().form_valid(form)


class MealsDeleteView(StaffRequiredMixin,DeleteView):
    model = Meals
    template_name = 'meals_confirm_delete.html' 
    success_url = reverse_lazy('meals_list')

    def form_valid(self, form):
        messages.success(self.request, "Meal has been successfully deleted!")
        return super().form_valid(form)