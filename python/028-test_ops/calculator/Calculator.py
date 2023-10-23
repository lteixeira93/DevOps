import DisplayViewer


class Calculator:
    """This is a simple calculator"""

    def __init__(self, d_viewer_obj: DisplayViewer):
        """ Class Constructor"""
        self._display = d_viewer_obj

    def sum(self, a, b):
        """Function to Sum 2 digits"""
        sum_elem = a + b
        error_code = self._display.showValueOnScreen(sum_elem)

        if error_code == 0:
            retval = sum_elem
        else:
            retval = error_code

        return retval

    def subtract(self, a, b):
        """Function to Subtract 2 digits"""
        subtraction = a - b

        error_code = self._display.showValueOnScreen(subtraction)

        if error_code == 0:
            retval = subtraction
        else:
            retval = error_code

        return retval
