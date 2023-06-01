from rest_framework import serializers

from bunnies.models import Bunny, RabbitHole


class RabbitHoleSerializer(serializers.ModelSerializer):

    bunnies = serializers.PrimaryKeyRelatedField(many=True, queryset=Bunny.objects.all())
    bunny_count = serializers.SerializerMethodField()

    def get_bunny_count(self, obj):
        return obj.bunnies.count()

    class Meta:
        model = RabbitHole
        fields = ('location', 'bunnies', 'bunny_count', 'owner')


class BunnySerializer(serializers.ModelSerializer):

    home = serializers.SlugRelatedField(queryset=RabbitHole.objects.all(), slug_field='location')
    family_members = serializers.SerializerMethodField()

    def get_family_members(self, obj):
        rabbit_hole = obj.home
        family_bunnies = rabbit_hole.bunnies.exclude(id=obj.id)
        return family_bunnies.values_list('name', flat=True)

    def validate(self, attrs):
        home = attrs.get('home')
        if home and home.bunnies.count() >= home.bunnies_limit:
            raise serializers.ValidationError("Cannot exceed the limit of bunnies in the rabbit hole.")
        return attrs

    class Meta:
        model = Bunny
        fields = ('name', 'home', 'family_members')

