from rest_framework import serializers
from .models import Introduction, Footer


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = "__all__"
        # exclude = ['field1', ]


class IntroductionFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = "__all__"
