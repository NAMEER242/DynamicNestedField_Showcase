from DynamicNestedField.DynamicNestedField import DynamicNestedMixin
from rest_framework.permissions import IsAuthenticated
from DNF_Showcase.models import C, B, A


class C_Serializer(DynamicNestedMixin):
    class Meta:
        model = C
        fields = ['charfield']
        permission_classes = [IsAuthenticated]  # the general permission class.
        permission_classes_by_method = {
            'GET': [IsAuthenticated],
            'POST': [IsAuthenticated],
            'PUT': [IsAuthenticated],
            'DELETE': [IsAuthenticated],
            # and so on.
        }


class B_Serializer(DynamicNestedMixin):
    c = C_Serializer()

    class Meta:
        model = B
        fields = ['charfield', 'c']
        DNM_config = {  # DNM_config holds all the configuration needed.
            "c": {
                "filter": "id",
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
    b = B_Serializer(many=True)  # many=True for m2m.

    class Meta:
        model = A
        fields = ['charfield', 'b']
        DNM_config = {  # DNM_config holds all the configuration needed.
            "b": {
                "filter": "id",
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
