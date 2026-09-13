from django.shortcuts import render

def stu_view(req):
    s = "Hello Python"
    context = {
        'title': s,
        "name": "Maya",
        "age": "25"
    }
    return render(req, "home.html", context)

def course_view(req):
    context = {
        "python": {
            "course_name": "Advance Python",
            "course_fees": 5000,
            "title": {
                "t1": "Django",
                "t2": "Numpy"
            }
    }}
    return render(req, "course.html", context)
