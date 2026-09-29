from django.urls import path
from education.views import*

urlpatterns = [
    path("", home_view, name="home"),
    path("student_add/",student_add, name="student_add" ),
    path("student_list/", student_list, name="student_list"),
    path("student_delete/<str:p_id>/", student_delete_view, name="delete_student" ),
    path("student_update/<str:id>/", student_update, name="student_update"),

    path("add_result/", add_result, name="add_result" ),
    path("result_list/", result_list, name="result_list"),
    path("result_delete/<str:id>/", delete_result, name="delete_result" ),
    path("result_update/<str:id>/", update_result, name="update_result")
]