from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

# class LinkSerializer(serializers.Serializer):
    
#     id = serializers.IntegerField(read_only=True)
#     link_text = serializers.CharField()
#     link_status_code = serializers.BooleanField()

#     def create(self, data):
#         return Link.objects.create(**data)

#     def update(self, instance, data):
#         instance.link_text = data.get('link_text', instance.link_text)
#         instance.link_status_code = data.get('link_status_code', instance.link_status_code)

#         instance.save()
#         return instance
