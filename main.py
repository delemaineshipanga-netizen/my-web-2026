from pathlib import Path

import flet as ft
from pypdf import PdfReader

if not hasattr(ft, "Colors"):
    ft.Colors = ft.colors
if not hasattr(ft, "Icons"):
    ft.Icons = ft.icons

BASE_DIR = Path(__file__).resolve().parent
PROFILE_IMAGE_PATH = BASE_DIR / "WhatsApp Image 2026-06-13 at 18.00.09 (1).jpeg"
PROFILE_VIDEO_PATH = BASE_DIR.parent.parent / "WhatsApp Video 2026-06-13 at 18.56.49.mp4"
PDF_FILES = sorted(BASE_DIR.glob("matlab_*.pdf*"))


def load_pdf_documents():
    documents = []

    for pdf_path in PDF_FILES:
        reader = PdfReader(str(pdf_path))
        page_text_blocks = []

        for page_number, page in enumerate(reader.pages, start=1):
            page_text = (page.extract_text() or "").strip()
            if page_text:
                page_text_blocks.append(f"Page {page_number}\n{page_text}")
            else:
                page_text_blocks.append(f"Page {page_number}\n[No extractable text found]")

        first_page_text = reader.pages[0].extract_text() or ""
        preview_text = " ".join(first_page_text.split())[:220]
        title = preview_text or pdf_path.stem.replace("_", " ")

        documents.append(
            {
                "path": pdf_path,
                "filename": pdf_path.name,
                "title": title,
                "pages": len(reader.pages),
                "summary": preview_text,
                "full_text": "\n\n".join(page_text_blocks).strip(),
            }
        )

    return documents


PDF_DOCUMENTS = load_pdf_documents()

PAGE_BG = "#F4F7FB"
SURFACE_BG = "#FFFFFF"
NAV_BG = "#EAF8F6"
ACCENT_TEAL = "#0F766E"
ACCENT_SKY = "#2563EB"
ACCENT_AMBER = "#D97706"
ACCENT_ROSE = "#DB2777"
ACCENT_VIOLET = "#7C3AED"
ACCENT_MINT = "#D1FAE5"
ACCENT_LAVENDER = "#EDE9FE"
ACCENT_SAND = "#FFF7ED"


def main(page: ft.Page):
    page.title = "Simon Delemaine Shipanga | Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_width = 1200
    page.window_height = 800
    page.theme = ft.Theme(color_scheme_seed=ACCENT_TEAL)
    page.bgcolor = PAGE_BG

    def section_title(text, color=ACCENT_TEAL):
        return ft.Text(text, size=32, weight=ft.FontWeight.BOLD, color=color)

    def home_section():
        profile_content = (
            ft.Image(
                src=str(PROFILE_IMAGE_PATH),
                fit=ft.ImageFit.COVER,
                width=132,
                height=132,
            )
            if PROFILE_IMAGE_PATH.exists()
            else ft.Icon(ft.icons.PERSON, size=66)
        )

        return ft.Container(
            bgcolor=SURFACE_BG,
            border_radius=24,
            border=ft.border.all(1, ACCENT_MINT),
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Text("PROFILE", size=12, weight="bold", color=ACCENT_TEAL),
                        bgcolor=ACCENT_MINT,
                        padding=10,
                        border_radius=999,
                        width=110,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=profile_content,
                                width=140,
                                height=140,
                                bgcolor=ACCENT_MINT,
                                border_radius=70,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                alignment=ft.alignment.center,
                            ),
                            ft.Column(
                                [
                                    ft.Text("Simon Delemaine Shipanga", size=40, weight="bold", color=ACCENT_TEAL),
                                    ft.Text("Student No: 224164090", size=20, color=ACCENT_ROSE),
                                    ft.Text("Aspiring UI Designer & Engineering Student", size=18, italic=True, color=ACCENT_SKY),
                                ],
                                spacing=5,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=30,
                    ),
                    ft.Divider(height=40),
                    ft.Text("About Me", size=24, weight="bold"),
                    ft.Text(
                        "Dedicated student focused on bridging the gap between complex engineering systems and user-friendly interfaces. "
                        "Specializing in creating communication tools for industrial environments that enhance safety and efficiency.",
                        size=16,
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "View GitHub Evidence",
                                icon=ft.icons.CODE,
                                on_click=lambda _: page.launch_url("https://github.com"),
                            ),
                            ft.ElevatedButton("Contact Me", icon=ft.icons.EMAIL),
                        ],
                        spacing=20,
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=40,
        )

    def mecktek_section():
        video_player = (
            ft.Video(
                playlist=[ft.VideoMedia(resource=str(PROFILE_VIDEO_PATH.resolve()))],
                autoplay=False,
                show_controls=True,
                expand=True,
                fit=ft.ImageFit.CONTAIN,
            )
            if PROFILE_VIDEO_PATH.exists()
            else ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.icons.VIDEO_FILE, size=80, color=ft.colors.BLUE_GREY_200),
                        ft.Text("Video file not found", weight="bold"),
                        ft.Text(str(PROFILE_VIDEO_PATH), size=12, italic=True),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,
                alignment=ft.alignment.center,
            )
        )

        return ft.Container(
            bgcolor=SURFACE_BG,
            border_radius=24,
            border=ft.border.all(1, ACCENT_SAND),
            content=ft.Column(
                [
                    section_title("Project: Mecktek", ACCENT_AMBER),
                    ft.Container(
                        content=ft.Text("Role: Lead UI Designer", weight="bold", color=ft.colors.WHITE),
                        bgcolor=ACCENT_AMBER,
                        padding=10,
                        border_radius=999,
                    ),
                    ft.Text(
                        "Mecktek is a specialized communication platform designed for engineering companies. "
                        "It facilitates real-time interaction between workers, technicians, and supervisors to monitor "
                        "the physical condition of materials and equipment on-site.",
                        size=16,
                    ),
                    ft.Divider(height=30),
                    ft.Text("My Contributions:", size=20, weight="bold"),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.BRUSH),
                        title=ft.Text("User Interface Design"),
                        subtitle=ft.Text("Designed intuitive dashboards for technicians to report material stress and condition."),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.DASHBOARD_CUSTOMIZE),
                        title=ft.Text("User Experience Flow"),
                        subtitle=ft.Text("Mapped communication paths between field workers and supervisors for rapid response."),
                    ),
                    ft.Divider(height=30),
                    ft.Text("Video Demonstration:", size=20, weight="bold"),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("UI Design Showcase Video", weight="bold", size=20),
                                ft.Text(PROFILE_VIDEO_PATH.name, size=12, color=ACCENT_AMBER),
                                ft.Container(
                                    content=video_player,
                                    width=800,
                                    height=450,
                                    bgcolor="#101828",
                                    border_radius=15,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=12,
                        ),
                        width=800,
                        height=520,
                        bgcolor=ACCENT_SAND,
                        border_radius=15,
                        border=ft.border.all(2, ACCENT_AMBER),
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=40,
        )

    def matlab_hub_section():
        def build_pdf_cards(documents):
            cards = []

            for document in documents:
                cards.append(
                    ft.Card(
                        content=ft.Container(
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Column(
                                                [
                                                    ft.Text(document["title"], size=20, weight="bold"),
                                                    ft.Text(document["filename"], size=12, color=ft.colors.GREY_600),
                                                ],
                                                expand=True,
                                                spacing=2,
                                            ),
                                            ft.Text(f'{document["pages"]} page(s)', size=12, color=ft.colors.GREY_700),
                                            ft.ElevatedButton(
                                                "Open PDF",
                                                icon=ft.icons.OPEN_IN_NEW,
                                                on_click=lambda _, path=document["path"]: page.launch_url(path.resolve().as_uri()),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.Text(document["summary"] or "No preview text found.", size=14, italic=True),
                                    ft.Container(
                                        height=260,
                                        padding=12,
                                        bgcolor=ft.colors.BLUE_GREY_50,
                                        border_radius=10,
                                        content=ft.Column(
                                            [
                                                ft.Text(
                                                    document["full_text"] or "No extractable text was found in this PDF.",
                                                    size=13,
                                                )
                                            ],
                                            scroll=ft.ScrollMode.AUTO,
                                        ),
                                    ),
                                ],
                                spacing=12,
                            ),
                        ),
                    )
                )

            return cards

        pdf_cards = build_pdf_cards(PDF_DOCUMENTS)

        return ft.Container(
            bgcolor=SURFACE_BG,
            border_radius=24,
            border=ft.border.all(1, ACCENT_LAVENDER),
            content=ft.Column(
                [
                    section_title("MATLAB Hub", ACCENT_VIOLET),
                    ft.Text(
                        "The MATLAB Hub now shows all 8 uploaded PDF files directly, with readable text previews and open buttons.",
                        size=16,
                        color=ACCENT_VIOLET,
                    ),
                    ft.Divider(height=20),
                    ft.ListView(expand=True, spacing=16, controls=pdf_cards),
                ],
                expand=True,
            ),
            padding=40,
            expand=True,
        )

    def tech_blog_section():
        return ft.Container(
            bgcolor=SURFACE_BG,
            border_radius=24,
            border=ft.border.all(1, "#FBCFE8"),
            content=ft.Column(
                [
                    section_title("Technical Blog: Confidence in Concepts", ACCENT_ROSE),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Engineering Material Cost Analysis", size=22, weight="bold"),
                                    ft.Markdown(
                                        "Effective UI design in engineering requires an understanding of the underlying data. "
                                        "Our system uses specific mathematical notations to calculate material longevity and replacement costs:\n\n"
                                        "#### Cost Calculation Formula:\n"
                                        "The total estimated cost (C) is derived using the summation of individual material units (q) multiplied by unit price (p), plus overhead (O):\n\n"
                                        "**C = Σ (q_i × p_i) + O**\n\n"
                                        "#### Material Degradation Logic:\n"
                                        "To visualize condition status, we implement a threshold logic where status is 'Critical' if:\n"
                                        "**Condition Index (CI) < Threshold (T_min)**",
                                        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                                    ),
                                ],
                                spacing=15,
                            ),
                            padding=30,
                            bgcolor="#FFF1F2",
                            border_radius=18,
                        )
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Logic Flow & System Architecture", size=20, weight="bold"),
                                    ft.Markdown(
                                        "1. Worker detects material flaw.\n"
                                        "2. UI inputs data via **Mecktek Mobile Interface**.\n"
                                        "3. Supervisor receives real-time notification via **Flet-based Desktop Portal**.\n"
                                        "4. Action items generated automatically."
                                    ),
                                ],
                                spacing=10,
                            ),
                            padding=20,
                            bgcolor="#FDF2F8",
                            border_radius=18,
                        )
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=40,
        )

    content_area = ft.Container(content=home_section(), expand=True)

    def on_nav_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            content_area.content = home_section()
        elif selected_index == 1:
            content_area.content = mecktek_section()
        elif selected_index == 2:
            content_area.content = matlab_hub_section()
        elif selected_index == 3:
            content_area.content = tech_blog_section()
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        bgcolor=NAV_BG,
        indicator_color=ACCENT_MINT,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_OUTLINE,
                selected_icon=ft.icons.PERSON,
                label="Profile",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.DASHBOARD_OUTLINED,
                selected_icon=ft.icons.DASHBOARD,
                label="Mecktek UI",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SCHOOL_OUTLINED,
                selected_icon=ft.icons.SCHOOL,
                label="MATLAB Hub",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ARTICLE_OUTLINED,
                selected_icon=ft.icons.ARTICLE,
                label="Tech Blog",
            ),
        ],
        on_change=on_nav_change,
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
