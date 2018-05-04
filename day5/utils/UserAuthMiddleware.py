from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from uauth.models import Users


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 统一验证登录
        # return None或者不写就不执行以后的操作
        if request.path == '/st/addinf/':
            pass

        if request.path == '/uau/re/':
            return None
        if request.path !='/uau/lo/':
            ticket = request.COOKIES.get('ticket')
            if not ticket:
                return HttpResponseRedirect('/uau/lo/')
            users = Users.objects.filter(u_ticket=ticket)
            if not users:
                return HttpResponseRedirect('/uau/lo')
            # 登录信息都放这里面
            request.user = users[0]

    # def process_response(self,request):
    #     c = 0
    #     if request.path == '//' and request.method == 'POST':
    #         c += 1