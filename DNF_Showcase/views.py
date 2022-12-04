from DNF_Showcase.DynamicNestedField.src.DynamicNestedField.DynamicNestedField import NestedModelViewSet
from DNF_Showcase.models import C, B, A
from DNF_Showcase.serializers import C_Serializer, B_Serializer, A_Serializer


class C_ViewSet(NestedModelViewSet):
    """
    [✔]NestedModelViewSet is activated in this ViewSet.
    """
    queryset = C.objects.all()
    serializer_class = C_Serializer
    enable_filter_schema = True


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
