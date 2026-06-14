# Simon Delemaine Shipanga - Engineering UI Portfolio

This is a professional web portfolio built using the Flet (Python) framework. It showcases the **Mecktek** engineering communication app, specific UI/UX design contributions, MATLAB certifications, and technical engineering insights.

## Features
- **Profile Management**: Displays Student Name (Simon Delemaine Shipanga) and Student No (224164090).
- **Mecktek Project Showcase**: Detailed role description as a UI Designer for the material condition monitoring app.
- **Video Placeholder**: Dedicated space in the Mecktek section to add your UI demonstration video.
- **MATLAB Hub**: A grid-based experience section featuring 8 core MATLAB/Simulink achievements.
- **Technical Blog**: Documentation of engineering concepts using Markdown and mathematical notations.
- **Responsive Navigation**: Sidebar-based navigation for a professional "Software Dashboard" feel.

## Prerequisites
- Python 3.9 or higher
- `pip` (Python package manager)

## Installation

1.  **Clone or create the project folder**:
    Create a new directory for your portfolio.

2.  **Install dependencies**:
    Run the following command in your terminal:
    `pip install -r requirements.txt`

## How to Run

1.  **Start the application**:
    Execute the main script:
    `python main.py`

2.  **View in Browser**:
    Flet will open a native window. To view it as a web app in your browser, change the last line of `main.py` to:
    `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`

## How to Add Your Video
In the `mecktek_section()` function in `main.py`, locate the `# VIDEO PLACEHOLDER SPACE`.
To add a local video or a URL:
1. Ensure you have the `flet-video` requirements (if applicable to your OS).
2. Change the Container content to:
    `content=ft.Video(src="https://your-video-link.mp4", autoplay=False)`

## Project Structure
- `main.py`: Main entry point containing all UI views and logic.
- `requirements.txt`: List of necessary Python libraries.
- `README.md`: Setup and usage instructions.

## Troubleshooting
- **Flet not found**: Ensure you ran `pip install flet`.
- **Navigation issues**: Ensure all view functions (e.g., `home_section`) are correctly referenced in the `on_nav_change` handler.
- **Math Symbols**: The Markdown component handles standard characters; for complex LaTeX rendering, ensure your system has the required fonts.
