from rest_framework.permissions import IsAuthenticated
from DNF_Showcase.DynamicNestedField.src.DynamicNestedField.DynamicNestedField import DynamicNestedMixin
from DNF_Showcase.models import C, B, A


class C_Serializer(DynamicNestedMixin):
    class Meta:
        model = C
        fields = ['id', 'charfield']
        permission_classes = [IsAuthenticated]  # the general permission class.
        permission_classes_by_method = {
            'GET': [IsAuthenticated],
            'POST': [IsAuthenticated],
            'PUT': [IsAuthenticated],
            'DELETE': [IsAuthenticated],
            # and so on.
        }


class B_Serializer(DynamicNestedMixin):
    c = C_Serializer(required=False)

    class Meta:
        model = B
        fields = ['id', 'charfield', 'c']
        DNM_config = {  # DNM_config holds all the configuration needed.
            "c": {
                "filter": ["id"],
            }
        }
        permission_classes = [IsAuthenticated]  # the general permission class.
        permission_classes_by_method = {
            'GET': [IsAuthenticated],
            'POST': [IsAuthenticated],
            'PUT': [IsAuthenticated],
            'DELETE': [IsAuthenticated],
            # and so on.
        }


class A_Serializer(DynamicNestedMixin):
    b = B_Serializer(required=False, many=True)  # many=True for m2m.

    class Meta:
        model = A
        fields = ['id', 'charfield', 'b']
        DNM_config = {  # DNM_config holds all the configuration needed.
            "b": {
                "filter": ["id", "charfield"],
            }
        }
        permission_classes = [IsAuthenticated]  # the general permission class.
        permission_classes_by_method = {
            'GET': [IsAuthenticated],
            'POST': [IsAuthenticated],
            'PUT': [IsAuthenticated],
            'DELETE': [IsAuthenticated],
            # and so on.
        }
