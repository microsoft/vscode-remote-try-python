# Copilot Instructions for vscode-remote-try-python

## Overview
This is a minimal Flask web application demonstrating VS Code Dev Containers for Python development. It serves a single static HTML page at the root route, showcasing containerized development workflows.

## Architecture
- **Main App**: `app.py` - Simple Flask application with one route that serves static HTML
- **Static Assets**: `static/index.html` - Basic HTML page with "VS Code Rocks!" content
- **Dependencies**: `requirements.txt` - Contains only Flask (installed via postCreateCommand)
- **Dev Environment**: `.devcontainer/devcontainer.json` - Python 3.12 container with Code Spell Checker extension

## Key Patterns
- **Static File Serving**: Use `app.send_static_file("index.html")` for serving static assets from the `static/` directory
- **Minimal Routing**: Single route `@app.route("/")` pattern for simple apps
- **Flask Setup**: `app = Flask(__name__)` with no additional configuration
- **Port Configuration**: Runs on port 9000 as configured in devcontainer.json and launch.json

## Development Workflow
- **Run App**: `python -m flask run --port 9000 --no-debugger --no-reload` (terminal command)
- **Debug**: Set breakpoints in `app.py` and press F5 to launch debugger (uses launch.json config with FLASK_APP=app.py, host=0.0.0.0)
- **Port Access**: App available at `http://localhost:9000` (or forwarded URL in Codespaces); port labeled "Hello Remote World" with notify on auto-forward
- **Container Rebuild**: Use "Dev Containers: Rebuild Container" after changing devcontainer.json

## Conventions
- **File Structure**: Keep static assets in `static/` directory; no templates or blueprints used
- **Flask Config**: Basic setup with no blueprints, templates, or advanced features
- **Extensions**: Code Spell Checker extension installed for development; Python extension available via devcontainer image
- **Post-Create**: Dependencies installed automatically via `pip3 install -r requirements.txt`
- **Debug Settings**: FLASK_ENV=development, FLASK_DEBUG=0 (debugging handled by VS Code)

## Example Modifications
- Add new routes: `@app.route("/new") def new_page(): return "Hello"`
- Serve additional static files: Place in `static/` and reference via `app.send_static_file("filename")`
- Add Flask features: Import and use blueprints, templates, etc. as needed (not currently used)
- Update HTML: Modify `static/index.html` for different content

## Project-Specific Notes
- This is a demonstration repository for Dev Containers, not a production application
- No tests, CI/CD, or advanced Flask features implemented
- Focus on container development workflow rather than app complexity</content>
<parameter name="filePath">/workspaces/vscode-remote-try-python/.github/copilot-instructions.md