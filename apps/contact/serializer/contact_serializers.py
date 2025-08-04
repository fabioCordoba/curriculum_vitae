from apps.contact.models.contact import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "email",
            "phone_number",
            "address",
            "web",
            "linkendin",
            "github",
            "instagram",
        ]
