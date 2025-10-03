import reflex as rx
from My_Fitness_Pal_ML.componentes.navbar import navbar
from My_Fitness_Pal_ML.componentes.chat import chat_page
from My_Fitness_Pal_ML.componentes.calendario import calendario_page
from rxconfig import config








def index() -> rx.Component:
    return rx.container(
        navbar(),
        rx.vstack(
            rx.heading("Bienvenido a tu asistente de IA", size="9"),  
            rx.text(
                "Aquí encontrarás herramientas para nutrición, calendario y chat con IA. "
                "Explora el menú para comenzar.",
                size="4",
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
        ),

        
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="orange",
        gray_color="sage",
        panel_background="solid",
        
        
    )
   
        
   
)
app.add_page(index, route="/")
app.add_page(chat_page, route="/chat", title="Chat")
app.add_page(calendario_page, route="/calendario", title="Calendario")
