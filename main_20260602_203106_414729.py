import flet as ft

def main(page: ft.Page):
    page.title = "Web Portfolio - MATLAB & Vlogs"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 40
    page.scroll = "adaptive"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE)

    # --- Header ---
    header = ft.Container(
        content=ft.Column([
            ft.Text("My Professional Portfolio", size=45, weight=ft.FontWeight.BOLD),
            ft.Text("Individual Assessment | Flet Web Application", size=18, italic=True),
            ft.Divider(height=30),
        ]),
        margin=ft.margin.only(bottom=20)
    )

    # --- MATLAB Section Title ---
    matlab_title = ft.Text("MATLAB Projects (8 Reports)", size=28, weight=ft.FontWeight.W_600)

    # --- PDF Grid ---
    # Assuming files are named matlab_1.pdf to matlab_8.pdf in the assets folder
    pdf_names = [
        "Signal Analysis", "Control Systems", "Image Processing", 
        "Data Visualization", "Algorithm Design", "Circuit Simulation", 
        "Neural Networks", "Robotics Toolbox"
    ]
    
    pdf_grid = ft.ResponsiveRow(
        spacing=20,
        run_spacing=20,
    )

    for i, name in enumerate(pdf_names, 1):
        pdf_grid.controls.append(
            ft.Card(
                col={"sm": 12, "md": 6, "lg": 3},
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Icon(ft.icons.PICTURE_AS_PDF, color=ft.colors.RED_ACCENT, size=40),
                        ft.Text(f"Part {i}: {name}", weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Download PDF", 
                            icon=ft.icons.DOWNLOAD,
                            on_click=lambda e, idx=i: page.launch_url(f"/assets/matlab_{idx}.pdf")
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                )
            )
        )

    # --- Vlogs Section ---
    vlog_title = ft.Text("Video Logs (Vlogs)", size=28, weight=ft.FontWeight.W_600)
    
    vlog_row = ft.Row(
        wrap=True,
        spacing=30,
        controls=[
            ft.Card(
                width=350,
                content=ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.Image(src="https://picsum.photos/400/225", border_radius=10), # Placeholder thumbnail
                        ft.Text("Vlog 01: Project Introduction", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("Overview of my engineering process and MATLAB workflow."),
                        ft.TextButton("Watch Video", icon=ft.icons.PLAY_CIRCLE_FILL, on_click=lambda _: page.launch_url("https://youtube.com"))
                    ])
                )
            ),
            ft.Card(
                width=350,
                content=ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.Image(src="https://picsum.photos/400/225?2", border_radius=10),
                        ft.Text("Vlog 02: Final Presentation", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("Final walkthrough of all 8 MATLAB modules."),
                        ft.TextButton("Watch Video", icon=ft.icons.PLAY_CIRCLE_FILL, on_click=lambda _: page.launch_url("https://youtube.com"))
                    ])
                )
            )
        ]
    )

    # Adding everything to the page
    page.add(
        header,
        matlab_title,
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        pdf_grid,
        ft.Divider(height=50, color=ft.colors.TRANSPARENT),
        vlog_title,
        vlog_row,
        ft.Divider(height=50),
        ft.Text("© 2024 Individual Assessment Portfolio", text_align=ft.TextAlign.CENTER, color=ft.colors.GREY_500)
    )

# Important for web deployment: set assets_dir
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
