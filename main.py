import flet as ft
import asyncio

class PortafolioHacker:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "DAVID_VARGAS_OS v1.1"
        self.page.padding = 0
        self.page.bgcolor = "#0B0E14"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.color_neon = "#00FF41"
        self.color_tarjeta = "#161B22"
        
        # Elementos para animar
        self.titulo_nombre = ft.Text("", size=60, weight="bold", font_family="monospace")
        self.status_text = ft.Text("", color=self.color_neon, size=12, font_family="monospace")
        self.log_terminal = ft.Column(spacing=2)

        self.build()

    def build(self):
        # ===== NAVBAR =====
        self.navbar = ft.Container(
            bgcolor="#000000", padding=15,
            border=ft.border.only(bottom=ft.border.BorderSide(1, self.color_neon)),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                   ft.Row(
                        controls=[
                            ft.Image(
                                src="noni.svg", 
                                width=30, 
                                height=30, 
                                color=self.color_neon
                            ),
                            ft.Text(" >_ K4RM4", color=self.color_neon, weight="bold", size=20, font_family="monospace"),
                        ],
                        spacing=10
                    ),
                    
                    ft.Row([
                        ft.TextButton("INICIO", on_click=lambda _: self.cambiar(0), style=ft.ButtonStyle(color=self.color_neon)),
                        ft.TextButton("SERVICIOS", on_click=lambda _: self.cambiar(1), style=ft.ButtonStyle(color=self.color_neon)),
                        ft.TextButton("RESUMEN", on_click=lambda _: self.cambiar(2), style=ft.ButtonStyle(color=self.color_neon)),
                        ft.TextButton("CONTACTO", on_click=lambda _: self.cambiar(3), style=ft.ButtonStyle(color=self.color_neon)),
                    ])
                ]
            )
        )

        # ===== PESTAÑA 1: INICIO (IMAGEN MÁS ALEJADA) =====
        self.inicio = ft.Container(
            visible=True, 
            padding=ft.padding.only(left=60, right=60, top=50, bottom=50),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Columna de texto
                    ft.Column(
                        expand=True, spacing=20,
                        controls=[
                            self.status_text,
                            ft.Text("root@davidvargas:~$ whoami", size=18, color=self.color_neon, font_family="monospace"),
                            self.titulo_nombre,
                            ft.Text("INGENIERO DE SOFTWARE & ENTUSIASTA DE CIBERSEGURIDAD", size=18, italic=True, color=self.color_neon),
                            ft.Container(
                                content=ft.Text(
                                    "Estudiante de 3er semestre en la Universidad De Cundinamarca con base técnica (SENA) y experiencia en Diana Agrícola. "
                                    "Especializado en automatización y defensa de sistemas.",
                                    size=15, color=ft.Colors.GREY_400, width=500
                                ),
                                border=ft.border.only(left=ft.border.BorderSide(3, self.color_neon)),
                                padding=ft.padding.only(left=20)
                            ),
                            ft.Container(content=self.log_terminal, padding=10, bgcolor="#05070A", border_radius=5, width=400)
                        ]
                    ),
                    
                    # SEPARADOR EXTRA PARA ALEJAR LA FOTO
                    ft.Container(width=200), 
                    
                    # Columna de la foto
                    ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Container(
                                content=ft.Image(src="foto.png", width=350, height=350, fit="cover", border_radius=175),
                                border=ft.border.all(3, self.color_neon), border_radius=175, padding=5,
                                shadow=ft.BoxShadow(blur_radius=25, color=self.color_neon),
                            ),
                            ft.Container(height=15),
                            ft.Text("while(alive): code()", color=self.color_neon, font_family="monospace", italic=True),
                        ]
                    )
                ]
            )
        )

        # ===== PESTAÑA 2: SERVICIOS =====
        self.servicios = ft.Container(
            visible=False, padding=50,
            content=ft.Column([
                ft.Text("[ MÓDULO: SERVICIOS ]", size=28, weight="bold", color=self.color_neon, font_family="monospace"),
                self.card("Script Kiddie", "Exploración de vulnerabilidades y reconocimiento de redes.", "kali.svg"),
                self.card("Automatización", "Scripts en Python para optimización de procesos.", "python.svg"),
                self.card("Power User Android", "Root, custom ROMs y gestión ADB/Fastboot.", "android.svg"),
                self.card("UI/UX Moderno", "Interfaces dinámicas con Flet y Python.", "react.svg"),
                self.card("OOP", "Orientada a Objetos.", "opp.svg"),
                self.card("Tkinter", "Interfaces graficas", "tkinter.png"),
            ])
        )

        # ===== PESTAÑA 3: RESUMEN =====
        self.resumen = ft.Container(
            visible=False, padding=50,
            content=ft.Column([
                ft.Text("[ MÓDULO: HISTORIAL_TECNICO ]", size=28, weight="bold", color=self.color_neon, font_family="monospace"),
                ft.Text("EXPERIENCIA_LABORAL", color=self.color_neon, size=18, weight="bold"),
                self.card("Técnico | Diana Agrícola", "• Soporte remoto/presencial\n• Mantenimiento de Servidores\n• Gestión dispositivos móviles", "python.svg"),
                ft.Text("HABILIDADES_DEL_SISTEMA", color=self.color_neon, size=18, weight="bold"),
                self.skill("Ofimática Experta", 0.95),
                self.skill("Soporte & Hardware", 0.85),
                self.skill("Ciberseguridad", 0.45),
                self.skill("Desarrollo", 0.55),
            ])
        )

        # ===== PESTAÑA 4: CONTACTO (LINKS CORREGIDOS) =====
        self.contacto = ft.Container(
            visible=False, padding=50,
            expand=True,
            content=ft.Column([
                ft.Text("[ ESTABLECIENDO_CONEXIÓN ]", size=28, weight="bold", color=self.color_neon, font_family="monospace"),
                self.card("Email", "david.vargas.agri@email.com", "gmail.png", "mailto:david.vargas.agri@email.com"),
                self.card("GitHub", "https://github.com/daviderminso", "git.svg", "https://://github.com"),
                self.card("K4RM4", "Status: Active | Encrypted", "noni.svg"),
            ], spacing=15, scroll="auto")
        )

        self.page.add(self.navbar, ft.Column(expand=True, scroll="auto", controls=[self.inicio, self.servicios, self.resumen, self.contacto]))

    def card(self, titulo, texto, icono, url=None):
        def hover(e):
            e.control.border = ft.border.all(2, self.color_neon if e.data == "true" else "#30363D")
            e.control.shadow = ft.BoxShadow(blur_radius=15, color=self.color_neon) if e.data == "true" else None
            e.control.update()

        return ft.Container(
            width=800,
            padding=15, bgcolor=self.color_tarjeta, border=ft.border.all(1, "#30363D"), border_radius=10,
            on_hover=hover, 
            on_click=lambda _: self.page.launch_url(url) if url else None,
            content=ft.Row([
                ft.Image(src=icono, width=40) if "." in icono else ft.Icon(icono, color=self.color_neon, size=30),
                ft.Column([ft.Text(titulo, weight="bold", color=self.color_neon, size=16), ft.Text(texto, color=ft.Colors.GREY_400, size=13)])
            ])
        )

    def skill(self, nombre, valor):
        return ft.Column([
            ft.Row([ft.Text(f"> {nombre}"), ft.Text(f"{int(valor*100)}%")], alignment="spaceBetween"),
            ft.Container(content=ft.ProgressBar(value=valor, color=self.color_neon, bgcolor="#1A1D23"), shadow=ft.BoxShadow(blur_radius=10, color=self.color_neon))
        ])

    async def animar_inicio(self):
        await self.escribir(self.status_text, "[ STATUS: ACTIVE ]  [ LOC: COLOMBIA ]  [ ROLE: ENG ]")
        await self.escribir(self.titulo_nombre, "David Vargas")
        logs = ["> [OK] Kernel loaded", "> [OK] System initialized", "> [OK] Security protocol: Active"]
        for log in logs:
            self.log_terminal.controls.append(ft.Text(log, color="#4A4E57", size=11, font_family="monospace"))
            self.page.update()
            await asyncio.sleep(0.3)

    async def escribir(self, control, texto):
        for i in range(len(texto) + 1):
            control.value = texto[:i] + "_"
            self.page.update()
            await asyncio.sleep(0.06)
        control.value = texto
        self.page.update()

    def cambiar(self, i):
        self.inicio.visible = (i == 0)
        self.servicios.visible = (i == 1)
        self.resumen.visible = (i == 2)
        self.contacto.visible = (i == 3)
        self.page.update()

async def main(page: ft.Page):
    app = PortafolioHacker(page)
    await app.animar_inicio()

ft.app(target=main,view=ft.AppView.WEB_BROWSER, assets_dir="assets")
