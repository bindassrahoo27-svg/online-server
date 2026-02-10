from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        # Ek vertical layout banate hain
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Ek Label (Text) add karte hain
        self.lbl = Label(text="Python App Build Success! 🚀", font_size='25sp')
        layout.add_widget(self.lbl)
        
        # Ek Button add karte hain
        btn = Button(text="Check Status", size_hint=(1, 0.2))
        btn.bind(on_press=self.on_click)
        layout.add_widget(btn)
        
        return layout

    def on_click(self, instance):
        # Button dabane par text badal jayega
        self.lbl.text = "GitHub Actions is Working! ✅"
        self.lbl.color = (0, 1, 0, 1) # Green color

if __name__ == '__main__':
    TestApp().run()
