from django.contrib.staticfiles.storage import ManifestFilesMixin, CachedFilesMixin

from pipeline.storage import PipelineMixin

from storages.backends.s3boto import S3BotoStorage


# In Django 1.7+ you should use ManifestFilesMixin unless you don’t have access to the local
# filesystem in which case you should use CachedFilesMixin.
class S3PipelineManifestStorage(PipelineMixin, ManifestFilesMixin, S3BotoStorage):
    pass


class S3PipelineCachedStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
    pass
