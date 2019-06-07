from wger.gym.models import Gym
from rest_framework import serializers

from wger.core.models import User


class GymTrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'is_active',
                  'id')
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


class GymSerializer(serializers.ModelSerializer):
    '''
    ScheduleStep serializer
    '''

    class Meta:
        model = Gym
        fields = '__all__'
