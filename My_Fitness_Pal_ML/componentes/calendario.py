import calendar
import datetime
import reflex as rx

from My_Fitness_Pal_ML.componentes.navbar import navbar


class CalendarState(rx.State):
    """Estado para el calendario interactivo."""
    year: int = datetime.date.today().year
    month: int = datetime.date.today().month
    selected_day: int | None = None
    new_event_text: str = ""
    events: dict[str, list[str]] = {}

    @rx.var
    def month_name(self) -> str:
        return calendar.month_name[self.month]
    
    @rx.var
    def month_year_display(self) -> str:
        return f"{self.month_name} {self.year}"

    @rx.var
    def selected_date_display(self) -> str:
        if self.selected_day is None:
            return "Seleccione una fecha"
        return f"{self.year}-{self.month:02d}-{self.selected_day:02d}"

    @rx.var
    def current_events(self) -> list[str]:
        if self.selected_day is None:
            return []
        key = f"{self.year}-{self.month:02d}-{self.selected_day:02d}"
        return self.events.get(key, [])

    def prev_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.selected_day = None

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.selected_day = None

    def select_day_1(self): self.selected_day = 1
    def select_day_2(self): self.selected_day = 2
    def select_day_3(self): self.selected_day = 3
    def select_day_4(self): self.selected_day = 4
    def select_day_5(self): self.selected_day = 5
    def select_day_6(self): self.selected_day = 6
    def select_day_7(self): self.selected_day = 7
    def select_day_8(self): self.selected_day = 8
    def select_day_9(self): self.selected_day = 9
    def select_day_10(self): self.selected_day = 10
    def select_day_11(self): self.selected_day = 11
    def select_day_12(self): self.selected_day = 12
    def select_day_13(self): self.selected_day = 13
    def select_day_14(self): self.selected_day = 14
    def select_day_15(self): self.selected_day = 15
    def select_day_16(self): self.selected_day = 16
    def select_day_17(self): self.selected_day = 17
    def select_day_18(self): self.selected_day = 18
    def select_day_19(self): self.selected_day = 19
    def select_day_20(self): self.selected_day = 20
    def select_day_21(self): self.selected_day = 21
    def select_day_22(self): self.selected_day = 22
    def select_day_23(self): self.selected_day = 23
    def select_day_24(self): self.selected_day = 24
    def select_day_25(self): self.selected_day = 25
    def select_day_26(self): self.selected_day = 26
    def select_day_27(self): self.selected_day = 27
    def select_day_28(self): self.selected_day = 28
    def select_day_29(self): self.selected_day = 29
    def select_day_30(self): self.selected_day = 30
    def select_day_31(self): self.selected_day = 31

    def add_event(self):
        if self.selected_day is None or not self.new_event_text.strip():
            return
        
        key = f"{self.year}-{self.month:02d}-{self.selected_day:02d}"
        if key not in self.events:
            self.events[key] = []
        self.events[key].append(self.new_event_text.strip())
        self.new_event_text = ""

    def set_new_event_text(self, value: str):
        self.new_event_text = value


def create_day_button(day_num: int, handler) -> rx.Component:
    """Crea un botón para un día específico del calendario."""
    if day_num == 0:
        return rx.box(height="60px", width="100%")
    
    return rx.box(
        rx.text(str(day_num)),
        padding="8px",
        height="60px",
        width="100%",
        border="1px solid #e2e8f0",
        border_radius="md",
        bg=rx.cond(CalendarState.selected_day == day_num, "#3182ce", "white"),
        color=rx.cond(CalendarState.selected_day == day_num, "white", "black"),
        cursor="pointer",
        _hover={"bg": rx.cond(CalendarState.selected_day == day_num, "#63b3ed", "#f7fafc")},
        on_click=handler,
        display="flex",
        align_items="flex-start",
        justify_content="flex-start"
    )


def calendario_page() -> rx.Component:
    """Página principal del calendario."""
    # Headers de días de la semana
    weekday_headers = [
        rx.box(rx.text("Lun", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
        rx.box(rx.text("Mar", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
        rx.box(rx.text("Mié", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
        rx.box(rx.text("Jue", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
        rx.box(rx.text("Vie", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
        rx.box(rx.text("Sáb", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
        rx.box(rx.text("Dom", font_weight="bold"), padding="8px", text_align="center", bg="#f7fafc"),
    ]

    # Crear calendario simple con días del 1 al 31
    calendar_days = [
        create_day_button(1, CalendarState.select_day_1),
        create_day_button(2, CalendarState.select_day_2),
        create_day_button(3, CalendarState.select_day_3),
        create_day_button(4, CalendarState.select_day_4),
        create_day_button(5, CalendarState.select_day_5),
        create_day_button(6, CalendarState.select_day_6),
        create_day_button(7, CalendarState.select_day_7),
        create_day_button(8, CalendarState.select_day_8),
        create_day_button(9, CalendarState.select_day_9),
        create_day_button(10, CalendarState.select_day_10),
        create_day_button(11, CalendarState.select_day_11),
        create_day_button(12, CalendarState.select_day_12),
        create_day_button(13, CalendarState.select_day_13),
        create_day_button(14, CalendarState.select_day_14),
        create_day_button(15, CalendarState.select_day_15),
        create_day_button(16, CalendarState.select_day_16),
        create_day_button(17, CalendarState.select_day_17),
        create_day_button(18, CalendarState.select_day_18),
        create_day_button(19, CalendarState.select_day_19),
        create_day_button(20, CalendarState.select_day_20),
        create_day_button(21, CalendarState.select_day_21),
        create_day_button(22, CalendarState.select_day_22),
        create_day_button(23, CalendarState.select_day_23),
        create_day_button(24, CalendarState.select_day_24),
        create_day_button(25, CalendarState.select_day_25),
        create_day_button(26, CalendarState.select_day_26),
        create_day_button(27, CalendarState.select_day_27),
        create_day_button(28, CalendarState.select_day_28),
        create_day_button(29, CalendarState.select_day_29),
        create_day_button(30, CalendarState.select_day_30),
        create_day_button(31, CalendarState.select_day_31),
    ]

    # Panel de eventos simplificado
    eventos_panel = rx.box(
        rx.heading("Eventos", size="5"),
        rx.text(CalendarState.selected_date_display, color="gray.600"),
        rx.cond(
            CalendarState.selected_day != None,
            rx.vstack(
                rx.hstack(
                    rx.input(
                        value=CalendarState.new_event_text,
                        placeholder="Agregar nuevo evento...",
                        on_change=CalendarState.set_new_event_text,
                        flex="1"
                    ),
                    rx.button(
                        "Agregar",
                        on_click=CalendarState.add_event,
                        color_scheme="blue"
                    ),
                    spacing="2",
                    width="100%"
                ),
                rx.foreach(
                    CalendarState.current_events,
                    lambda event: rx.box(
                        rx.text(event),
                        padding="8px",
                        border="1px solid #e2e8f0",
                        border_radius="md",
                        width="100%"
                    )
                ),
                spacing="3",
                width="100%"
            ),
            rx.text("Seleccione un día para ver o agregar eventos", color="gray.500")
        ),
        padding="20px",
        border="1px solid #e2e8f0",
        border_radius="md",
        bg="white",
        width="100%"
    )

    return rx.container(
        navbar(),
        rx.vstack(
            # Header con controles de navegación
            rx.hstack(
                rx.button("◀", on_click=CalendarState.prev_month, variant="outline"),
                rx.heading(CalendarState.month_year_display, size="6", text_align="center", flex="1"),
                rx.button("▶", on_click=CalendarState.next_month, variant="outline"),
                spacing="4",
                align="center",
                width="100%"
            ),
            
            # Calendario
            rx.vstack(
                rx.grid(*weekday_headers, template_columns="repeat(7, 1fr)", gap="1px", width="100%"),
                rx.grid(*calendar_days, template_columns="repeat(7, 1fr)", gap="1px", width="100%"),
                spacing="0",
                width="100%"
            ),
            
            # Panel de eventos
            eventos_panel,
            
            spacing="6",
            width="100%",
            padding="20px"
        ),
        max_width="800px",
        center_content=True
    )
