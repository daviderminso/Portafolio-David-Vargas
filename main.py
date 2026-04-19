import flet as ft
import asyncio
import webbrowser 

class PortafolioHacker:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "DAVID_VARGAS_OS v1.1"
        self.page.padding = 0
        self.page.bgcolor = "#0D1117"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.color_neon = "#00D166"
        self.color_tarjeta = "#161B22"
        
        self.verde_pro = "#00D166"    # Verde esmeralda para acentos (Navbar, Iconos, Bordes)
        self.blanco_pro = "#E4EBE5"   # El blanco que ya te gustó para los textos
        self.color_tarjeta = "#161B22"
        
        # Elementos para animar
        self.titulo_nombre = ft.Text("", size=60, weight="bold", font_family="Retrofont")
        self.status_text = ft.Text("", color=self.color_neon, size=12, font_family="monospace")
        self.log_terminal = ft.Column(spacing=2)

        self.build()
        
    
        
        
    def chip_tecnico(self, texto, destacado=False):
        """Crea etiquetas estéticas para las habilidades"""
        return ft.Container(
            content=ft.Text(
                texto, 
                color="#000000" if destacado else self.blanco_pro, 
                size=11, 
                weight="bold",
                font_family="monospace"
            ),
            bgcolor=self.verde_pro if destacado else ft.Colors.with_opacity(0.1, self.verde_pro),
            border=None if destacado else ft.border.all(1, self.verde_pro),
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            border_radius=5,
        )
        
    def abrir_whatsapp(self, e):
        import webbrowser
        webbrowser.open("https://wa.me/573125400171")
        
    def abrir_proyectos(self, e):
        webbrowser.open("https://github.com/daviderminso/Programacion_II_-16_Pasos_Tkinter")


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
                                color=self.blanco_pro
                            ),
                            ft.Text(" >_ K4RM4", color=self.blanco_pro, weight="bold", size=20, font_family="monospace"),
                        ],
                        spacing=10
                    ),
                    
                    ft.Row([
                        ft.TextButton("INICIO", on_click=lambda _: self.cambiar(0), style=ft.ButtonStyle(color=self.blanco_pro)),
                        
                        ft.TextButton("SERVICIOS", on_click=lambda _: self.cambiar(1), style=ft.ButtonStyle(color=self.blanco_pro)),
                        ft.TextButton("RESUMEN", on_click=lambda _: self.cambiar(2), style=ft.ButtonStyle(color=self.blanco_pro)),
                        ft.TextButton("CONTACTO", on_click=lambda _: self.cambiar(3), style=ft.ButtonStyle(color=self.blanco_pro)),
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
                        expand=True, spacing=25,
                        controls=[
                            self.status_text,
                            ft.Text("root@davidvargas:~$ whoami", size=18, color=self.blanco_pro, font_family="monospace"),
                            self.titulo_nombre,
                            ft.Text("INGENIERO DE SOFTWARE & ENTUSIASTA DE CIBERSEGURIDAD", size=18, italic=True, color=self.verde_pro),
                            ft.Container(
                                
                                content=ft.Text(
                                    spans=[
                                            ft.TextSpan("Ingeniero de Software en formación con perfil técnico experto. ", ft.TextStyle(color=ft.Colors.WHITE)),
                                            ft.TextSpan("Especializado en la creación de herramientas de automatización con Python (POO, Flet, Tkinter) ", ft.TextStyle(color=self.verde_pro, weight="bold")),
                                            ft.TextSpan("y en la gestión avanzada de sistemas Android (Root, Custom ROMs, ADB).", ft.TextStyle(color=ft.Colors.WHITE)),
                                            ft.TextSpan("Enfocado en la ciberseguridad, la auditoría de vulnerabilidades y la eficiencia de sistemas críticos.", ft.TextStyle(color=self.verde_pro)),
                                    ],
                                    size=14, 
                                    color=ft.Colors.GREY_400, 
                                    width=700, # Un poco más ancho para que se lea mejor el bloque
                                    font_family="Retrofont"
                                ),
                                
                                border=ft.border.only(left=ft.border.BorderSide(3, self.color_neon)),
                                padding=ft.padding.only(left=20)
                            ),
                            ft.Row(
                                controls=[
                                    self.chip_tecnico("Python", True),
                                    self.chip_tecnico("Flet"),
                                    self.chip_tecnico("Android Root"),
                                    self.chip_tecnico("Linux"),
                                    self.chip_tecnico("Git"),
                                ],
                                spacing=15
                            ),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        "Descargar CV.exe",
                                        icon=ft.Icons.FILE_DOWNLOAD_OUTLINED,
                                        on_click=self.abrir_proyectos,
                                        style=ft.ButtonStyle(
                                            color=self.verde_pro,
                                            bgcolor="#161B22",
                                            side= ft.border.BorderSide(1, self.verde_pro),
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                        
                                        
                                        ),
                                    ),
                                    ft.TextButton(
                                    "Ver Proyectos",
                                    icon=ft.Icons.CODE_ROUNDED,
                                    on_click=lambda _: self.cambiar(1),
                                    style=ft.ButtonStyle(color=self.blanco_pro),
                                ),
                           
                                ],
                                spacing=20
                            ),
                            

                            
                            ft.Container(content=self.log_terminal, padding=10, bgcolor="#05070A", border_radius=5, width=400, border= ft.border.all(1, "#1A1A1A"))
                        ]
                    ),
                    
                    
                    
                    # SEPARADOR EXTRA PARA ALEJAR LA FOTO
                    ft.Container(width=200), 
                    
                                       # ===== Columna de la foto (Lado Derecho) =====
                    ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            # 1. Contenedor de la Foto
                            ft.Container(
                                content=ft.Image(src="foto_sin.png", width=600, height=350,),
                                 
                                
                                
                            ),
                            
                            ft.Container(height=20), # Bajamos un poco el espacio
                            ft.Text("Si no salió bien a la primera, llámalo versión 1.0", color=self.blanco_pro, font_family="Retrofont", size= 12, italic=True),
                            ft.Container(height=20),
                            
                            # Módulo del Personaje Animado
                                ft.Image(
                                    src="what.gif", # Si tuvieras el gif
                                    width=300,
                                    height=50,
                                ),
                            
                            # 2. Terminal Kali Linux para WhatsApp
                            ft.Container(
                                width=350,
                                bgcolor="#0D1117",
                                border=ft.border.all(1, "#30363D"),
                                border_radius=10,
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        # Barra Superior de la Ventana
                                        ft.Container(
                                            bgcolor="#161B22",
                                            padding=ft.padding.symmetric(horizontal=10, vertical=8),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    ft.Row(
                                                        spacing=5,
                                                        controls=[
                                                            ft.Container(width=12, height=12, bgcolor="#FF5F56", border_radius=6),
                                                            ft.Container(width=12, height=12, bgcolor="#FFBD2E", border_radius=6),
                                                            ft.Container(width=12, height=12, bgcolor="#27C93F", border_radius=6),
                                                        ]
                                                    ),
                                                    ft.Text("terminal — Whatsapp@kali: ~", size=11, color=ft.Colors.GREY_400, font_family="monospace"),
                                                ]
                                            )
                                        ),
                                        # Cuerpo de la Terminal
                                        ft.Container(
                                            padding=15,
                                            content=ft.Column(
                                                spacing=10,
                                                controls=[
                                                    ft.Text("kali@host:~$ ./whatsapp_bot.py", size=12, color=self.verde_pro, font_family="monospace"),
                                                    ft.Text("[SYSTEM] initializing chat_module...", size=11, color=self.blanco_pro, font_family="monospace"),
                                                    ft.Text("[READY] Conexión establecida.", size=11, color=self.blanco_pro, font_family="monospace"),
                                                    ft.Container(height=5),
                                                    # Botón de WhatsApp
                                                    ft.ElevatedButton(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(ft.Icons.CHAT_ROUNDED, size=18),
                                                                ft.Text(" ABRIR CHAT", weight="bold", font_family="Retrofont"),
                                                            ]
                                                        ),
                                                        style=ft.ButtonStyle(
                                                            color="#000000",
                                                            bgcolor=self.verde_pro,
                                                            shape=ft.RoundedRectangleBorder(radius=5),
                                                        ),
                                                        on_click=self.abrir_whatsapp
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    ) # Fin de la Columna de la foto
                ] # Fin de controls del Row principal
            ) # Fin de content del Container inicio
        ) # Fin de self.inicio

        
    

        # ===== PESTAÑA 2: SERVICIOS =====
        self.servicios = ft.Container(
            visible=False, padding=50,
            content=ft.Column([
                ft.Text("[ MÓDULO: SERVICIOS ]", size=28, weight="bold", color=self.verde_pro, font_family="monospace"),
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
                self.card("GitHub", "https://github.com/daviderminso", "git.svg", "https://github.com/daviderminso"),
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
        await self.escribir(self.status_text, "[ STATUS: ACTIVE ]  [ LOC: UNKNOWN_PROXY ]  [ ROLE: ENG ]")
        await self.escribir(self.titulo_nombre, "David Vargas")
        logs = ["> [OK] Kernel loaded", "> [OK] System initialized", "> [OK] Security protocol: Active"]
        for log in logs:
            self.log_terminal.controls.append(ft.Text(log, color="#4A4E57", size=11, font_family="monospace"))
            self.page.update()
            await asyncio.sleep(0.2)

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
    # 1. Registro de fuentes
    page.fonts = {
        "Retrofont": "2p.ttf", # Verifica que en la carpeta assets se llame exactamente así
    }
    
    # 2. Inicializar la clase
    app = PortafolioHacker(page)
    
    # 3. ¡IMPORTANTE! Agregar los paréntesis ()
    page.update() 
    
    # 4. Iniciar la animación
    await app.animar_inicio()

if __name__ == "__main__":
    # Mantengo tu configuración de navegador web
    ft.app(
        target=main, 
        view=ft.AppView.WEB_BROWSER, 
        port=8080, 
        assets_dir="assets" )# Aquí es donde Flet buscará el archivo 2.ttf

