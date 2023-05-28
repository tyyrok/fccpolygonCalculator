class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture." 
        else:
        # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line.
            pass

    def get_amount_inside(self, shape):
        # Take another shape and return the number of times it could fit inside the shape
        pass

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        return self.set_side(width)
    
    def set_height(self, height):
        return self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
