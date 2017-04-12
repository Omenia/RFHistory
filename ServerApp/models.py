from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TestRun(models.Model):
    name = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    upload_time = models.DateTimeField()
    source_file = models.CharField(max_length=500)
    version_info = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name


class TestCase(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class TestCaseExecution(models.Model):
    test_case = models.ForeignKey(TestCase)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    error_message = models.TextField(blank=True, null=True)


class TestRunTestExecutions(models.Model):
    test_run_id = models.ForeignKey(TestRun)
    test_case_execution_id = models.ForeignKey(TestCaseExecution)


class Suite(models.Model):
    name = models.CharField(max_length=500)
    doc = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class ChildSuites(models.Model):
    parent_suite = models.ForeignKey(Suite)
    child_suite = models.ForeignKey(Suite)


class SuiteTestCases(models.Model):
    suite = models.ForeignKey(Suite)
    test_case = models.ForeignKey(TestCase)


class Tag(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class TestCaseExecutionTags(models.Model):
    test_case_execution = models.ForeignKey(TestCaseExecution)
    tag = models.ForeignKey(Tag)


class Keyword(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class KeywordExecution(models.Model):
    keyword = models.ForeignKey(Keyword)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    error_message = models.TextField(blank=True, null=True)


class TestCaseExecutionKeywords(models.Model):
    test_case_execution = models.ForeignKey(TestCaseExecution)
    keyword_execution = models.ForeignKey(KeywordExecution)


class KeywordLibrary(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class LibraryKeywords(models.Model):
    library = models.ForeignKey(KeywordLibrary)
    keyword = models.ForeignKey(Keyword)
