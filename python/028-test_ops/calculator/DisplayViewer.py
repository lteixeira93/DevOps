class DisplayViewer:
    """This is a simple class that print values to the screen"""

    def __init__(self, error_code):
        self.errorCode = error_code

    def showValueOnScreen(self, value):
        print("Display Result: ", value)
        return self.errorCode
