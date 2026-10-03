#!/usr/bin/env python3
"""
ROKY V2.1 - PHASE 1
Basic Android app with Kivy GUI
Simple chat UI - hardcoded responses only (no AI yet)
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from datetime import datetime


class RokyApp(App):
    """Roky Phase 1 - Basic UI only"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Roky V2.1'
        self.conversation = []
    
    def build(self):
        """Build the UI"""
        
        # Main container
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.08)
        title = Label(
            text='🤖 ROKY V2.1',
            font_size='18sp',
            bold=True
        )
        header.add_widget(title)
        
        # Chat display (scrollable)
        chat_container = BoxLayout(size_hint_y=0.75)
        chat_scroll = ScrollView()
        self.chat_display = Label(
            text='Roky: Hello! I\'m Roky. Type something!\n',
            size_hint_y=None,
            markup=True
        )
        self.chat_display.bind(texture_size=self.chat_display.setter('size'))
        chat_scroll.add_widget(self.chat_display)
        chat_container.add_widget(chat_scroll)
        
        # Input area
        input_layout = BoxLayout(size_hint_y=0.12, spacing=10)
        self.input_field = TextInput(
            hint_text='Type here...',
            multiline=False,
            size_hint_x=0.8
        )
        self.input_field.bind(on_text_validate=self.send_message)
        
        send_button = Button(
            text='Send',
            size_hint_x=0.2
        )
        send_button.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.input_field)
        input_layout.add_widget(send_button)
        
        # Add all to main
        main_layout.add_widget(header)
        main_layout.add_widget(chat_container)
        main_layout.add_widget(input_layout)
        
        return main_layout
    
    def send_message(self, instance):
        """Handle message send"""
        
        message = self.input_field.text.strip()
        
        if not message:
            return
        
        # Add user message to display
        self.chat_display.text += f'You: {message}\n'
        self.conversation.append(('user', message))
        
        # Clear input
        self.input_field.text = ''
        
        # Get demo response (hardcoded for Phase 1)
        response = self.get_demo_response(message)
        
        # Add Roky response to display
        self.chat_display.text += f'Roky: {response}\n\n'
        self.conversation.append(('roky', response))
    
    def get_demo_response(self, user_input):
        """
        PHASE 1: Hardcoded responses only
        (Real AI comes in Phase 2)
        """
        
        message = user_input.lower().strip()
        
        # Simple keyword matching
        if 'hello' in message or 'hi' in message:
            return 'Hey there! 👋 I\'m Roky. Nice to meet you!'
        
        elif 'what' in message and 'do' in message:
            return 'Phase 1 features: Chat UI. Phase 2 coming: AI, voice, memory!'
        
        elif 'roky' in message:
            return 'That\'s me! I\'m your AI assistant. 🤖'
        
        elif 'help' in message:
            return 'I can chat with you! Try: "Hello", "What can you do?", "Tell me a joke"'
        
        elif 'joke' in message:
            return 'Why did the Python go to the gym? To get more bytes! 💪'
        
        elif 'time' in message:
            now = datetime.now()
            return f'Current time: {now.strftime("%H:%M:%S")}'
        
        else:
            return f'You said: "{user_input}". I\'m learning! Phase 2 will have real AI. 🧠'


if __name__ == '__main__':
    app = RokyApp()
    app.run()
