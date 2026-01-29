
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class AI_UI(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = 'vertical'
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._upd, pos=self._upd)
        self.add_widget(Label(text="ABDOU AI FACTORY v1.0", font_size='24sp', color=(0, 0.7, 1, 1), bold=True))
        self.add_widget(Label(text="Status: AI Engine Evolution Active", font_size='16sp'))

    def _upd(self, inst, val):
        self.rect.pos = inst.pos
        self.rect.size = inst.size

class AbdouApp(App):
    def build(self): return AI_UI()

if __name__ == '__main__': AbdouApp().run()
