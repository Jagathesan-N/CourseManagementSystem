from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Feedback
from .forms import FeedbackForm

# Show all courses with feedback count
def course_list(request):
    courses = Course.objects.all()
    courses_with_count = []

    for course in courses:
        count = course.feedbacks.count()  # Make sure Feedback model has related_name="feedbacks"
        courses_with_count.append({
            "course": course,
            "feedback_count": count
        })

    return render(request, "courses/course_list.html", {"courses_with_count": courses_with_count})

# Show a specific course + feedback
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # Handle feedback form submission
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.course = course  # Link feedback to this course
            feedback.save()
            return redirect("course_detail", course_id=course.pk)  # Prevent re-post on refresh
    else:
        form = FeedbackForm()

    # Get all feedback for this course
    feedbacks = course.feedbacks.all()

    return render(request, "courses/course_detail.html", {
        "course": course,
        "form": form,
        "feedbacks": feedbacks,
    })
