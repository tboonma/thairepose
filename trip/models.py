from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TripPlan(models.Model):
    """Extended user model class that use for Trip plan.

    Attributes:
        title(str): title of post
        author(user): user who write post
        body(str): descriptions
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    duration = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        """Return redirect to all trip pages."""
        return reverse("trip:tripdetail", args=(str(self.id)))


class Review(models.Model):
    """Extended user model class that use for Review.

    Attributes:
        post(TripPlan): trip plan that host of review
        name(str): name of who write commend
        date_added(datetime): date and time when comment writed
        like(object): file to store user to like comment
    """

    post = models.ForeignKey(
        TripPlan, related_name="review", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='commended', blank=True)

    @property
    def total_like(self):
        """Return number of count."""
        return self.like.count()

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name.username)

    def get_absolute_url(self):
        """Return redirect to detail of each commend.

        When your like comment page will refesh itseft to show all like.
        """
        return reverse("trip:tripdetail", args=(str(self.post.id)))
