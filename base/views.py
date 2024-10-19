from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout


from .models import Task

def home(request):
    return render(request, "base/home.html")

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"

    # def get_queryset(self):
    #     return self.model.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(owner=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__startswith = search_input)
        context["search_input"] = search_input
        return context

class TaskCreate(CreateView):
    model = Task
    context_object_name = "tasks"
    fields = ["title", "description", "complete"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")

def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account has been created, Login in now"{username}"')
            return redirect("login")
    else:
            form = UserCreationForm()
    return render(request, "base/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')  # or any other page you want to redirect logged-in users to
        return super().get(request, *args, **kwargs)
    
class TaskUpdate(UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect("login")


class TaskUpdateComplete(UpdateView):
    model = Task
    fields = ["complete"]
    template_name = "base/task_update_complete.html"
    success_url = reverse_lazy("task-list")

