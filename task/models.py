from django.db import models
from django.conf import settings


class Task(models.Model):
    NONE = "NO"
    LOW = "LO"
    MEDIUM = "ME"
    HIGH = "HI"

    CHOICE_PRIORITY = [
        (NONE, "Non"),
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High")
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    notes = models.TextField()
    due_date = models.DateTimeField(db_index=True)
    priority = models.CharField(max_length=2,
                                choices=CHOICE_PRIORITY,
                                default=NONE,
                                db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    passed = models.BooleanField(default=False)     # Indicates whether the task is done or not