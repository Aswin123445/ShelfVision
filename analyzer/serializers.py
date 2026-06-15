from rest_framework import serializers


class ShelfLayoutSerializer(serializers.Serializer):
    layout = serializers.ListField()

    def validate_layout(self, value):
        """
        Expected format:
        [
            ["G", "G", "M"],
            ["G", "B", "M"]
        ]
        """

        # Check empty layout
        if not value:
            raise serializers.ValidationError("Layout cannot be empty.")

        # Check first row exists
        if not isinstance(value[0], list):
            raise serializers.ValidationError("Layout must be a 2D array.")

        row_length = len(value[0])

        # Check row length
        if row_length == 0:
            raise serializers.ValidationError("Rows cannot be empty.")

        for row in value:

            if not isinstance(row, list):
                raise serializers.ValidationError("Each row must be a list.")

            if len(row) != row_length:
                raise serializers.ValidationError("All rows must have the same length.")

            for cell in row:

                if not isinstance(cell, str):
                    raise serializers.ValidationError("Each cell must be a string.")

                if len(cell) != 1:
                    raise serializers.ValidationError(
                        "Each cell must contain exactly one character."
                    )

                if not cell.isupper() or not cell.isalpha():
                    raise serializers.ValidationError(
                        "Only uppercase letters A-Z are allowed."
                    )

        return value
