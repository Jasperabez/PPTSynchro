from win32com import client

class PptHandler:
    def __init__(self):
        self.win32 = client

    def GrabPptSession(self):
        try:
            self.ppt_app = self.win32.GetActiveObject("PowerPoint.Application")
            self.active_ppt = self.ppt_app.activePresentation.SlideShowWindow
            return True
        except Exception as ex:
            return False

    def NextSlide(self):
        self.active_ppt.View.Next()

    def PrevSlide(self):
        self.active_ppt.View.Previous()
        
