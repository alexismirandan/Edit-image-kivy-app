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

    # Widht and Height of selected rectangle (line drawn with touch)
    width_selected = NumericProperty(0)
    height_selected = NumericProperty(0)

    # Widht and Height old of selected rectangle (line drawn with touch)
    width_selected_old = ObjectProperty(0)
    height_selected_old = ObjectProperty(0)

    # Line Color and width
    line_color = ListProperty([1, 1, 1, 1])
    line_width = NumericProperty(3)

    # First tap in TouchSelector
    first_tap = True
    
    def __init__(self, *args, **kwargs):
        super(TouchSelector, self).__init__(*args, **kwargs)
        #Bind list_lines_in_image attribute 
        self.bind(list_lines_in_image=self.remove_old_line)
        self.register_event_type('on_change_size')

    def on_touch_up(self, touch):
        self.set_width_height()
        if self.first_tap:
            self.first_tap = False

    def on_change_size(self):
        pass

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

    def set_width_height(self):
        width = abs(self.Cx - self.Dx)
        height = abs(self.Cy - self.By)

        if self.first_tap or self.width_selected != 0 and self.height_selected != 0:
            dispatch_on_change_size = False
            if self.first_tap or width != self.width_selected and height != self.height_selected:
                dispatch_on_change_size = True

            self.width_selected = width if width != 0 else self.width_selected
            self.height_selected = height if height != 0 else self.height_selected

            if dispatch_on_change_size:
                self.dispatch('on_change_size')

            self.width_selected_old = self.width_selected
            self.height_selected_old = self.height_selected

    def tap_not_draw_a_line(self):
        """
        When touchdown is called and tap not draw a line.
        """
        return (self.width_selected_old == self.width_selected and self.height_selected_old == self.height_selected)
