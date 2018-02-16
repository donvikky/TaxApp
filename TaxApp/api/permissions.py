from rest_framework import permissions


class IsOwnerOrIsAdmin(permissions.IsAuthenticated):
    '''Allow only admin user'''

    OBJECT_OWNER_FIELD = 'user'

    def has_object_permission(self, request, view, obj):
        # Allow admins to view/edit/delete objects
        if request.user and request.user.is_staff:
            return True

        # Allow owners to view/edit/delete objects
        if hasattr(obj, self.OBJECT_OWNER_FIELD):
            return getattr(obj, self.OBJECT_OWNER_FIELD) == request.user

        return False
