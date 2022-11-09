from DNF_Showcase.models import C, B, A
from DNF_Showcase.serializers import C_Serializer, B_Serializer, A_Serializer
from Tools.DynamicNestedMixin import NestedModelViewSet


class C_ViewSet(NestedModelViewSet):
    """
    [✔]NestedModelViewSet is activated in this ViewSet.
    """
    queryset = C.objects.all()
    serializer_class = C_Serializer


class B_ViewSet(NestedModelViewSet):
    """
    [✔]NestedModelViewSet is activated in this ViewSet.
    """
    queryset = B.objects.all()
    serializer_class = B_Serializer


class A_ViewSet(NestedModelViewSet):
    """
    [✔]NestedModelViewSet is activated in this ViewSet.
    """
    queryset = A.objects.all()
    serializer_class = A_Serializer
