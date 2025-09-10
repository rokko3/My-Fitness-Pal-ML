import reflex as rx
def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading("Chatbot IA", size="6"),
        rx.spacer(),
        rx.link("Inicio", href="/", padding_x="2"),
        rx.link("Nutrición", href="/nutricion", padding_x="2"),
        rx.link("Calendario", href="/calendario", padding_x="2"),
        rx.link("Chat", href="/chat", padding_x="2"),
        rx.link("Login", href="/login", padding_x="2"),
        spacing="5",
        padding="4",
        border_bottom="1px solid #eaeaea",
    )