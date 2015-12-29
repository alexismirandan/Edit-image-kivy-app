# -*- coding: utf-8 -*
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.graphics import Line, Color

class TouchSelector(Widget):
    # Points of Line object
    Ax = NumericProperty(0)
    Ay = NumericProperty(0)
    Bx = NumericProperty(0)
    By = NumericProperty(0)
    Cx = NumericProperty(0)
    Cy = NumericProperty(0)
    Dx = NumericProperty(0)
    Dy = NumericProperty(0)

    # Object line
    line = ObjectProperty()

    # List of line objects drawn
    list_lines_in_image = ListProperty([])

    # Widht and Height of selected rectangle (line drawn with touch)
    width_selected = NumericProperty(0)
    height_selected = NumericProperty(0)

    # Line Color and width
    line_color = ListProperty([1, 1, 1, 1])
    line_width = NumericProperty(3)
    
    def __init__(self, *args, **kwargs):
        super(TouchSelector, self).__init__(*args, **kwargs)
        #Bind list_lines_in_image attribute 
        self.bind(list_lines_in_image=self.remove_old_line)

    def on_touch_up(self, touch):
        self.width_selected = abs(self.Cx - self.Dx)
        self.height_selected = abs(self.Cy - self.By)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(self.line_color)

            # Save initial tap position
            self.Ax, self.Ay = touch.x, touch.y

            # Initilize positions to save
            self.Bx, self.By = 0, 0
            self.Cx, self.Cy = 0, 0
            self.Dx, self.Dy = 0, 0

            # Create initial point with touch x and y postions.
            self.line = Line(points=([self.Ax, self.Ay]), width=self.line_width, joint='miter', joint_precision=30)

            # Save the created line
            self.list_lines_in_image.append(self.line)

    def remove_old_line(self, instance, list_lines):
        """Remove the old line draw"""
        if len(list_lines) > 1:
            list_lines.pop(0).points = []

    def on_touch_move(self, touch):
        # Assign the position of the touch at the point C
        self.Cx, self.Cy = touch.x, touch.y

        # There are two known points A (starting point) and C (endpoint)
        # Assign the  positions x and y  known of the points
        self.Bx, self.By = self.Cx, self.Ay
        self.Dx, self.Dy = self.Ax, self.Cy

        # Assign points positions to the last line created
        self.line.points = [self.Ax, self.Ay,
                            self.Bx, self.By,
                            self.Cx, self.Cy,
                            self.Dx, self.Dy,
                            self.Ax, self.Ay]
