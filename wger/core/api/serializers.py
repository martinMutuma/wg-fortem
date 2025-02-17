# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

from rest_framework import serializers

from wger.core.models import (
    UserProfile,
    Language,
    DaysOfWeek,
    License,
    RepetitionUnit,
    WeightUnit)
from django.contrib.auth.models import User


class UserprofileSerializer(serializers.ModelSerializer):
    '''
    Workout session serializer
    '''
    class Meta:
        model = UserProfile
        fields = []


class UsernameSerializer(serializers.Serializer):
    '''
    Serializer to extract the username
    '''
    username = serializers.CharField()


class LanguageSerializer(serializers.ModelSerializer):
    '''
    Language serializer
    '''
    class Meta:
        model = Language
        fields = []


class DaysOfWeekSerializer(serializers.ModelSerializer):
    '''
    DaysOfWeek serializer
    '''
    class Meta:
        model = DaysOfWeek
        fields = []


class LicenseSerializer(serializers.ModelSerializer):
    '''
    License serializer
    '''
    class Meta:
        model = License
        fields = []


class RepetitionUnitSerializer(serializers.ModelSerializer):
    '''
    Repetition unit serializer
    '''
    class Meta:
        model = RepetitionUnit
        fields = []


class WeightUnitSerializer(serializers.ModelSerializer):
    '''
    Weight unit serializer
    '''
    class Meta:
        model = WeightUnit
        fields = []


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ User register serializer """

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}, 'username': {'min_length': 3}}
