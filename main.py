from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from plyer import notification


class NotificationApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.text_input = TextInput(hint_text='Enter your message', multiline=False)
        layout.add_widget(self.text_input)

        send_button = Button(text='Send Notification')
        send_button.bind(on_press=self.send_notification)
        layout.add_widget(send_button)

        return layout

    def send_notification(self, instance):
        message = self.text_input.text.strip()
        if message:
            notification.notify(
                title='New Message',
                message=message,
                app_name='NotificationApp',
                timeout=10
            )
            self.text_input.text = ''


if __name__ == '__main__':
    NotificationApp().run()
