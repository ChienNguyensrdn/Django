from django.core.management.base import BaseCommand
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from app_admin.models import Course
from app_admin.document import CourseDocument

class Command(BaseCommand):
    help = "Index data from Product model into Elasticsearch"

    def handle(self, *args, **kwargs):
        es = connections.get_connection()
        bulk(
            client=es,
            actions=(
                CourseDocument(
                    meta={'id': Course.id},
                    name = Course.name,
                    description = Course.description,
                    year = Course.year,
                    startDate = Course.startDate,
                    endDate = course.endDate,
                ).to_dict(True) for course in Course.objects.all()
            )
        )
        self.stdout.write(self.style.SUCCESS('Indexed all Courses'))
