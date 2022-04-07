from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

class IsSalesUserOrReadOnly(permissions.BasePermission):

    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:
            return True

        # Permission are only allowed to the owner of the Sales staff or manager
        return obj.sales_contact_id == request.user.id or IsAdminUser

