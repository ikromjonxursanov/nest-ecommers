from django.db import models

class OrderStatusChoices(models.IntegerChoices):
    NEW = 1,  "New"
    ACCEPTED = 2, "Accepted"
    REJECTED = 3, "Rejected"
    DELIVERED = 4, "Delivered"