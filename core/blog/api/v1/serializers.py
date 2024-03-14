from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content"]


class PostDetailSerializer(serializers.ModelSerializer):
    # ---------------------------------------------------
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    # ---------------------------------------------------
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    # ---------------------------------------------------
    absolute_url = serializers.SerializerMethodField()
    # ---------------------------------------------------
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = "__all__"
        # ---------------------------------------------------
        # read_only_fields = ['content']
        # ---------------------------------------------------
        read_only_fields = ["author"]
        # ---------------------------------------------------

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # ---------------------------------------------------------
        representation["category"] = CategorySerializer(instance=instance.category).data
        # ---------------------------------------------------------
        reqeust = self.context.get("request")
        if reqeust.parser_context.get("kwargs").get("pk"):
            representation.pop("snippet", None)
            representation.pop("relative_url", None)
            representation.pop("absolute_url", None)
        else:
            representation.pop("content", None)
        # ---------------------------------------------------------
        return representation

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
