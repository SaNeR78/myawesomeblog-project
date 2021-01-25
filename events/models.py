from django.db import models

# Create your models here.

class Event(models.Model):
	event_title = models.CharField(max_length=100)
	event_image = models.ImageField(upload_to='event_images/')
	event_text = models.TextField()
	event_date = models.DateTimeField(auto_now_add=True)

	def get_summary(self):
		if len(self.event_text) <= 70:
			text = self.event_text[:70]
		else:
			text = self.event_text[:70] + '...'

		return text
