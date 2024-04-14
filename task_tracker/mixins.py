from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
	def dispatch(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.creator != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


# class DashboardMixin:
# 	def get_context_data(self,**kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context["dashboard_pk"] = self.kwargs.get("dashboard_pk", None)
# 		return context