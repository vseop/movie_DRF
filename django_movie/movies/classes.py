from rest_framework import mixins, viewsets


class MixedPermission:
    """Миксин permissions для action"""

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CreateUpdateDestroyListMy(mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.ListModelMixin,
                                MixedPermission,
                                viewsets.GenericViewSet):
    """"""
    pass
