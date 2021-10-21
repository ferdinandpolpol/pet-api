from web.models import Pet
from rest_framework import serializers


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age']

    def create(self, validated_data):
        # TODO, move into a django model where species can be customized
        allowed_species = ["cat", "dog"]
        species = validated_data.get("species")
        species_is_allowed = species in allowed_species
        
        if not species_is_allowed:
            raise serializers.ValidationError(
                f"Specie {species} not in allowed. Allowed {allowed_species}")

        return Pet(**validated_data)