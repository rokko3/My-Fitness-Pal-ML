"""Index con barra de navegación para chatbot de IA."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """El estado de la app."""


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


def index() -> rx.Component:
    return rx.container(
        navbar(),
        rx.vstack(
            rx.heading("Bienvenido a tu asistente de IA", size="9"),  
            rx.text(                                                 
                "Aquí encontrarás herramientas para nutrición, calendario y chat con IA. "
                "Explora el menú para comenzar.",
                size="4",
                color="gray.600",
            ),
            rx.box(
                rx.text("Inicio: La página principal donde encontrarás un resumen general de la aplicación."),
                rx.text("Nutrición: Registra y consulta tu alimentación diaria con recomendaciones personalizadas."),
                rx.text("Calendario: Organiza tus rutinas y controla tu progreso a lo largo del tiempo."),
                rx.text("Chat: Conversa con un asistente inteligente que responde tus preguntas."),
                rx.text("Login: Accede a tu perfil y configura tu experiencia personal."),
                margin_top="20px",
                padding="4",
            )

        )
    )


app = rx.App()
app.add_page(index, route="/")
