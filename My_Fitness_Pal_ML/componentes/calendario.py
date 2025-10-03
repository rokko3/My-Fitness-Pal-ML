import calendar
import datetime
import reflex as rx

from My_Fitness_Pal_ML.componentes.navbar import navbar

# ----------------- Constantes -----------------
WEEKDAYS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
CELL_SIZE = 160          # Tamaño de cada celda (px)
BORDER_COLOR = "#000"    # Color de bordes principal


class CalendarState(rx.State):
    """Estado del calendario con soporte básico de eventos y CRUD de eventos diarios."""

    year: int = datetime.date.today().year
    month: int = datetime.date.today().month
    selected_day: int | None = None
    new_event_text: str = ""
    events: dict[str, list[str]] = {}

    # -------- Helpers internos --------
    def _last_day(self) -> int:
        return calendar.monthrange(self.year, self.month)[1]

    def _day_key(self) -> str | None:
        if not self.selected_day:
            return None
        return f"{self.year}-{self.month:02d}-{self.selected_day:02d}"

    # -------- Vars derivadas --------
    @rx.var
    def month_year(self) -> str:
        return f"{calendar.month_name[self.month]} {self.year}"

    @rx.var
    def days_rows(self) -> list[list[int]]:
        """Filas secuenciales: 1..7, 8..14, etc. (row-major)."""
        last_day = self._last_day()
        rows = (last_day + 6) // 7  # ceil sin importar math
        matrix: list[list[int]] = []
        day = 1
        for _ in range(rows):
            row: list[int] = []
            for _ in range(7):
                row.append(day if day <= last_day else 0)
                day += 1
            matrix.append(row)
        return matrix

    @rx.var
    def selected_label(self) -> str:
        return (
            f"{self.year}-{self.month:02d}-{self.selected_day:02d}"
            if isinstance(self.selected_day, int)
            else "Seleccione un día"
        )

    @rx.var
    def current_events(self) -> list[str]:
        key = self._day_key()
        return self.events.get(key, []) if key else []

    # -------- Navegación --------
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

    # -------- Acciones de interacción --------
    def select_day(self, day: int):
        if isinstance(day, dict) or not isinstance(day, int) or day == 0:
            return
        self.selected_day = day

    def set_new_event_text(self, value: str):
        self.new_event_text = value

    def add_event(self):
        key = self._day_key()
        txt = self.new_event_text.strip()
        if not key or not txt:
            return
        self.events.setdefault(key, []).append(txt)
        self.new_event_text = ""

    def delete_event(self, ev: str):
        key = self._day_key()
        if not key:
            return
        if ev in self.events.get(key, []):
            self.events[key].remove(ev)
            if not self.events[key]:
                del self.events[key]


# ----------------- Render de celdas -----------------
def day_cell(day: int | rx.Var) -> rx.Component:
    """Render de una celda de día (vacía si day == 0)."""
    base_styles = dict(
        height=f"{CELL_SIZE}px",
        width=f"{CELL_SIZE}px",
        border_radius="6px",
        transition="all 0.15s ease",
    )
    return rx.cond(
        day == 0,
        rx.box(
            "",
            bg="#f1f5f9",
            border=f"1px solid {BORDER_COLOR}",
            **base_styles,
        ),
        rx.box(
            rx.text(
                day,
                font_size="22px",
                font_weight="bold",
                margin_bottom="8px",
                color=rx.cond(CalendarState.selected_day == day, "white", "black"),
            ),
            padding="8px",
            bg=rx.cond(CalendarState.selected_day == day, "#2563eb", "white"),
            color=rx.cond(CalendarState.selected_day == day, "white", "black"),
            border=rx.cond(
                CalendarState.selected_day == day,
                "2px solid #1d4ed8",
                f"1px solid {BORDER_COLOR}",
            ),
            cursor="pointer",
            _hover={"bg": rx.cond(CalendarState.selected_day == day, "#1d4ed8", "#e2e8f0")},
            display="flex",
            flex_direction="column",
            align_items="flex-start",
            justify_content="flex-start",
            gap="4px",
            on_click=lambda _day=day: CalendarState.select_day(_day),
            **base_styles,
        ),
    )


# ----------------- Matriz de calendario -----------------
def calendar_matrix() -> rx.Component:
    """Filas secuenciales (1..7, 8..14, ...) con encabezado de días de la semana."""
    header = rx.hstack(
        *[
            rx.box(
                rx.text(dia, font_weight="bold", font_size="16px", color="black"),
                width=f"{CELL_SIZE}px",
                text_align="center",
            )
            for dia in WEEKDAYS
        ],
        spacing="3",
        align="start",
    )

    rows = rx.foreach(
        CalendarState.days_rows,
        lambda fila: rx.hstack(
            rx.foreach(fila, day_cell),
            spacing="3",
            align="start",
        ),
    )

    return rx.vstack(header, rows, spacing="3", width="100%", align="start")


# ----------------- Panel de eventos -----------------
def events_panel() -> rx.Component:
    return rx.box(
        rx.heading("Eventos", size="5", color="black"),
        rx.text(CalendarState.selected_label, color="black"),
        rx.cond(
            CalendarState.selected_day != None,
            rx.vstack(
                rx.hstack(
                    rx.input(
                        value=CalendarState.new_event_text,
                        placeholder="Nuevo evento...",
                        on_change=CalendarState.set_new_event_text,
                        flex="1",
                    ),
                    rx.button("Agregar", on_click=CalendarState.add_event, size="2"),
                    spacing="2",
                    width="100%",
                ),
                rx.foreach(
                    CalendarState.current_events,
                    lambda ev: rx.hstack(
                        rx.text(ev, flex="1"),
                        rx.button(
                            "X",
                            on_click=lambda ev_text=ev: CalendarState.delete_event(ev_text),
                            size="1",
                            color_scheme="red",
                            variant="outline",
                        ),
                        align="center",
                        width="100%",
                        padding="6px 8px",
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="6px",
                        gap="8px",
                    ),
                ),
                spacing="3",
                width="100%",
            ),
            rx.text("Seleccione un día para gestionar eventos", color="gray.500"),
        ),
        padding="16px",
        border=f"1px solid {BORDER_COLOR}",
        border_radius="8px",
        bg="white",
        width="100%",
        max_width="420px",
    )


# ----------------- Página principal -----------------
def calendario_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.hstack(
                rx.button("◀", on_click=CalendarState.prev_month, variant="outline", size="3"),
                rx.heading(CalendarState.month_year, size="6", flex="1", text_align="center", color="black"),
                rx.button("▶", on_click=CalendarState.next_month, variant="outline", size="3"),
                width="100%",
                align="center",
                padding_y="8px",
                padding_x="12px",
                bg="#f1f5f9",
                border_radius="8px",
                gap="12px",
            ),
            rx.hstack(
                calendar_matrix(),
                events_panel(),
                align="start",
                spacing="5",
                width="100%",
                flex="1",
                flex_wrap="wrap",
            ),
            spacing="5",
            width="100%",
            padding="16px",
            max_width="1500px",
            margin="0 auto",
            flex="1",
        ),
        display="flex",
        flex_direction="column",
        width="100%",
        min_height="100vh",
        bg="#e2e8f0",
        padding_bottom="24px",
    )
