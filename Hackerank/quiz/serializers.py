from rest_framework import serializers
from quiz.models import Category,Questions,Answers

class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    is_active=serializers.CharField(read_only=True)
    class Meta:
        model=Category
        fields="__all__"


class AnswerSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    # question=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields=["id","options","is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    choices=AnswerSerializer(read_only=True,many=True)
    class Meta:
        model=Questions
        fields=["id","category","mode","mark","question","choices"]
