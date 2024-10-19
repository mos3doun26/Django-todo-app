from django.urls import path, reverse_lazy
from .views import TaskList, TaskCreate, TaskDetail, TaskDelete, Register, CustomLoginView, home, TaskUpdate, logout_view, TaskUpdateComplete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home" ),
    path("tasks/", TaskList.as_view(), name="task-list" ),
    path("tasks/new-task/", TaskCreate.as_view(), name="new-task" ),
    path("tasks/task/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("tasks/delete/<int:pk>/", TaskDelete.as_view(), name="task-delete" ),
    path("tasks/update/<int:pk>/", TaskUpdate.as_view(http_method_names=["post", "get", "options"]), name="task-update" ),
    # path('logout/', auth_views.LogoutView.as_view( template_name = "base/logout.html",next_page='login', http_method_names=["post", "get", "options"]), name='logout'),
    path("tasks/update-complete/<int:pk>/",TaskUpdateComplete.as_view(), name="task-update-complete" ),
    path("login/", CustomLoginView.as_view(), name="login" ),
    path('logout/', logout_view, name='logout'),
    path("register/", Register, name="register" ),
]