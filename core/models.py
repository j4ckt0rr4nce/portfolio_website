from django.db import models


SLUZBY_CHOICES = [
        ('Služby', 'Služby'),
        ('Django', 'Django'),
        ('React', 'React'),
        ('Html/CSS', 'Html/CSS'),
    ]

class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    service = models.CharField(choices=SLUZBY_CHOICES, default='Služby', max_length=20)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"



class Contact(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.subject}"



BLOG_CHOICES = [
        ('Blog_1', 'Blog_1'),
        ('Blog_2', 'Blog_2'),
        ('Blog_3', 'Blog_3'),
    ]

class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    website = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    avatar = models.ImageField(default='avatar.png')
    blog_no = models.CharField(choices=BLOG_CHOICES, max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	    return f"{self.blog_no} - {self.name}"

    def num_replies(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)



class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField()
    url = models.CharField(max_length=40)
    day = models.IntegerField(default=0)
    month = models.CharField(max_length=10)
    year = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	    return str(self.title)
