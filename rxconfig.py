import reflex as rx

config = rx.Config(
    app_name="My_Fitness_Pal_ML",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)