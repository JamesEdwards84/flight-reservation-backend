import re
from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation

# Custom validator 3
def validate_flight(data):
    print(data)
    return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [validate_flight] # 3

    # Custom validator 1
    def validate_flightNumber(self, flightNumber):
        if re.match("^[a-zA-Z0-9]*$", flightNumber) is None:
            raise serializers.ValidationError("Invalid Flight Number. Should be alphanumeric.")
        return flightNumber

    # Custom validator 2
    def validate(self, data):
        print(data)
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'