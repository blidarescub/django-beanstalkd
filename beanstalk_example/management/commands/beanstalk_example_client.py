from django.core.management.base import BaseCommand
from django_beanstalkd import BeanstalkClient


class Command(BaseCommand):
    help = "Execute an example command with the django_beanstalk_jobs interface"
    __doc__ = help

    def handle(self, *args, **options):
        client = BeanstalkClient()

        print "Asynchronous Beanstalk Call"
        print "-------------------------"
        print "Notice how this app exits, while the workers still work on the tasks."
        for i in range(4):
            client.call(
                'beanstalk_example.background_counting', '5'
            )
