from django.urls import path
from .views import TaskList, TaskCreate, TaskDelete, Register, CustomLoginView, home, TaskUpdate, logout_view, profile

urlpatterns = [
    path("", home, name="home" ),
    path("tasks/", TaskList.as_view(), name="task-list" ),
    path("tasks/new-task/", TaskCreate.as_view(), name="new-task" ),
    path("tasks/delete/<int:pk>/", TaskDelete.as_view(), name="task-delete" ),
    path("tasks/update/<int:pk>/", TaskUpdate.as_view(http_method_names=["post", "get", "options"]), name="task-update" ),
    path("login/", CustomLoginView.as_view(), name="login" ),
    path('logout/', logout_view, name='logout'),
    path("register/", Register, name="register" ),
    path("profile/", profile, name="profile" ),

]
