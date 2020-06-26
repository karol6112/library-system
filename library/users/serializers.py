from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    def validate(self, data):
        id_number = data['id_number']

        if len(id_number) != 9:
            raise serializers.ValidationError('ID NUMBER is too short or long')

        SERIA_DATE = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
            'G': 16,
            'H': 17,
            'I': 18,
            'J': 20,
            'K': 21,
            'L': 22,
            'M': 23,
            'N': 24,
            'O': 25,
            'P': 26,
            'R': 27,
            'S': 28,
            'T': 29,
            'U': 30,
            'W': 31,
            'X': 32,
            'Y': 33,
            'Z': 34,
        }

        WEIGHT = [7, 3, 1, 7, 3, 1, 7, 3]

        sum = 0
        control_digit = int(id_number[3])
        number = []
        try:
            for x in id_number[:3]:
                number.append(SERIA_DATE[x])

            number += [int(i) for i in id_number[4:]]

            number = zip(number, WEIGHT)

            for d, w in number:
                sum += d * w
        except:
            raise serializers.ValidationError('ID NUMBER is not correct. Wrong format')

        if sum % 10 == control_digit:
            return data
        else:
            raise serializers.ValidationError('ID NUMBER is not correct')

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'id_number',
        )

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'username': {'min_length': 3},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'id_number',
        )

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'id_number',
            'is_active',
        )
