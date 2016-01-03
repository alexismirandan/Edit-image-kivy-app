# -*- coding: utf-8 -*
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.graphics import Line, Color
from components import image

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

    # Size of the selected rectangle
    size_selected = ListProperty([0,0])

    # Size previous of the selected rectangle
    size_selected_previous = ListProperty([0,0])

    # Size temporary of the selected rectangle
    size_selected_temp = ListProperty([0,0])

    # Line Color and width
    line_color = ListProperty([1, 1, 1, 1])
    line_width = NumericProperty(3)

    # First tap in TouchSelector
    first_tap = True
    
    def __init__(self, *args, **kwargs):
        super(TouchSelector, self).__init__(*args, **kwargs)
        self.bind(list_lines_in_image=self.remove_old_line)

    def on_touch_up(self, touch):
        self.size_selected = abs(self.Cx - self.Dx), abs(self.Cy - self.By)
        self.size_selected_previous = self.size_selected

    def on_touch_down(self, touch):
        with self.canvas:
            Color(self.line_color)

            # Save initial tap position
            self.Ax, self.Ay = self.first_touch_x, self.first_touch_y = touch.x, touch.y

            # Initilize positions to save
            self.Bx, self.By = 0, 0
            self.Cx, self.Cy = 0, 0
            self.Dx, self.Dy = 0, 0

            # Create initial point with touch x and y postions.
            self.line = Line(points=([self.Ax, self.Ay]), width=self.line_width, joint='miter', joint_precision=30)

            # Save the created line
            self.list_lines_in_image.append(self.line)

    def remove_old_line(self, instance=None, list_lines=None):
        """Remove the old line draw"""
        if len(self.list_lines_in_image) > 1:
            self.delete_line()

    def delete_line(self, pos=0):
        try:
            self.list_lines_in_image.pop(pos).points = []
        except: pass

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

        self.size_selected_temp = abs(self.Cx - self.Dx), abs(self.Cy - self.By)

    def tap_not_draw_a_line(self):
        """
        When touchdown is called and tap not draw a line.
        """
        return (self.size_selected[0] == 0 and self.size_selected[1] == 0)
