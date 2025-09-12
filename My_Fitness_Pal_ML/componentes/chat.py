import reflex as rx

from My_Fitness_Pal_ML.componentes.navbar import navbar
class ChatState(rx.State):
    """Estado para manejar el chat."""
    messages: list[tuple[str, str]] = [] 
    current_message: str = ""

    def send_message(self):
        """Enviar mensaje al chat."""
        if self.current_message.strip():
            # Agregamos mensaje del usuario
            self.messages.append(("usuario", self.current_message))
            # Respuesta simulada de la IA (puedes reemplazar con un modelo real)
            self.messages.append(("ia", f"Aca viene la respuesta de chat: {self.current_message}"))
            self.current_message = ""

def chat_page() -> rx.Component:
    return rx.container(
        navbar(),
        rx.box(
            rx.vstack(
                # Área de mensajes
                rx.scroll_area(
                    rx.foreach(
                        ChatState.messages,
                        lambda msg: rx.box(
                            rx.text(
                                msg[1],
                                size="4",
                                color=rx.cond(msg[0] == "usuario", "red", "black"),
                            ),
                            padding="3",
                            border_radius="lg",
                            bg=rx.cond(msg[0] == "usuario", "blue.500", "gray.200"),
                            max_width="70%",
                            align_self=rx.cond(msg[0] == "usuario", "end", "start"),
                            margin_y="2",
                        )
                    ),
                    height="70vh",
                    padding="4",
                ),
                # Input para enviar mensaje
                rx.hstack(
                    rx.input(
                        value=ChatState.current_message,
                        placeholder="Escribe tu mensaje...",
                        on_change=ChatState.set_current_message,
                        width="100%",
                    ),
                    rx.button("Enviar", on_click=ChatState.send_message),
                    spacing="3",
                    width="100%",
                    padding="2",
                ),
                spacing="4",
                width="100%",
            ),
            width="100%",
            padding="4",
        ),
    )
