from django.utils.deprecation import MiddlewareMixin
from stu.models import Visit
import logging

logger = logging.getLogger('auth')


class visit(MiddlewareMixin):

    def process_request(self, request):

        # 访问url次数
        path = request.path
        try:
            vis = Visit.objects.get(v_url=path)
            if vis:
                vis.v_time += 1
                vis.save()
        except Exception as e:
            logger.error(e)
            Visit.objects.create(v_url=path, v_time=1)
