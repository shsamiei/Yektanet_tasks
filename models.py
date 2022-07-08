from django.db import models



class Advertiser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, default=' ')
    link = models.CharField(max_length=200, default=' ')
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    pub_date = models.DateTimeField('date published')
    approve = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class View(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    viewed_time = models.DateTimeField('date viewed')


class Click(models.Model):
    clicked_time = models.DateTimeField('date clicked')
    Ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class ClickedCount(models.Model):
    begin_time = models.DateTimeField(default=None, null=True)
    end_time = models.DateTimeField(default=None, null=True)
    count = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, default=None, null=True)


class ViewedCount(models.Model):
    begin_time = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)
    count = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, default=None,  null=True)


