from haystack import indexes
from job.models import JobPost
import datetime



class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    post_date = indexes.DateTimeField(model_attr='post_date')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return JobPost

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

