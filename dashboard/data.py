"""Mock data to populate the dashboard charts and tables."""

import reflex as rx
from dashboard.graphs import Area, Line

stat_card_data = [
    [
        "Horas semanales registradas",
        "53",
        "+2%",
    ],
    [
        "Horas mensuales registradas",
        "240",
        "+5%",
    ],
    [
        "Retrasos semanales",
        "1",
        "-3%",
    ],
    [
        "Retrasos mensuales",
        "2",
        "+2%",
    ],
]

line_chart_data = [
    {"name": "Enero", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Febrero", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Marzo", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Abril", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Mayo", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Junio", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Julio", "uv": 3490, "pv": 4300, "amt": 2100},
]


lines = [
    Line(data_key="pv", stroke="#8884d8"),
    Line(data_key="uv", stroke="var(--accent-8)"),
]


pie_chart_data = [
    {"name": "Group A", "value": 400, "fill": "var(--red-7)"},
    {"name": "Group B", "value": 300, "fill": "var(--green-7)"},
    {"name": "Group C", "value": 300, "fill": "var(--purple-7)"},
    {"name": "Group D", "value": 200, "fill": "var(--blue-7)"},
    {"name": "Group E", "value": 278, "fill": "var(--yellow-7)"},
    {"name": "Group F", "value": 189, "fill": "var(--pink-7)"},
]

area_chart_data = line_chart_data

areas = [
    Area(data_key="pv", stroke="#8884d8", fill="#8884d8"),
    Area(data_key="uv", stroke="var(--accent-8)", fill="var(--accent-8)"),
]


tabular_data = [
    ["Full name", "Email", "Group"],
    ["Danilo Sousa", "danilo@example.com", rx.badge("Developer")],
    ["Zahra Ambessa", "zahra@example.com", rx.badge("Admin", variant="surface")],
    ["Jasper Eriksson", "jasper@example.com", rx.badge("Developer")],
]
