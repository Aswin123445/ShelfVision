from collections import defaultdict


class ShapeDetector:

    @classmethod
    def analyze(cls, layout):
        rows = len(layout)
        cols = len(layout[0])

        brands = defaultdict(list)

        # Collect coordinates for each brand
        for row in range(rows):
            for col in range(cols):
                brand = layout[row][col]
                brands[brand].append((row, col))

        result = {}

        for brand, coordinates in brands.items():

            shape = cls._detect_shape(coordinates)

            location = cls._detect_location(coordinates, rows, cols)

            result[brand] = {"shape": shape, "location": location}

        return result

    @staticmethod
    def _detect_shape(coordinates):
        rows = [row for row, _ in coordinates]
        cols = [col for _, col in coordinates]

        min_row = min(rows)
        max_row = max(rows)

        min_col = min(cols)
        max_col = max(cols)

        height = max_row - min_row + 1
        width = max_col - min_col + 1

        occupied_cells = len(coordinates)
        bounding_box_area = height * width

        # Not a complete rectangle
        if occupied_cells != bounding_box_area:
            return "polygon"

        # Complete rectangle
        if height == width:
            return "square"

        if height > width:
            return "vertical rectangle"

        return "horizontal rectangle"

    @staticmethod
    def _detect_location(coordinates, total_rows, total_cols):

        avg_row = sum(row for row, _ in coordinates) / len(coordinates)

        avg_col = sum(col for _, col in coordinates) / len(coordinates)

        # Vertical position
        if avg_row < total_rows / 3:
            vertical = "top"
        elif avg_row > (2 * total_rows) / 3:
            vertical = "bottom"
        else:
            vertical = "middle"

        # Horizontal position
        if avg_col < total_cols / 3:
            horizontal = "left"
        elif avg_col > (2 * total_cols) / 3:
            horizontal = "right"
        else:
            horizontal = "center"

        if vertical == "middle":
            return [horizontal]

        if horizontal == "center":
            return [vertical]

        return [f"{vertical} {horizontal}"]
