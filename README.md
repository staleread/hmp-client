# 🎵 HearMyPaper

**Secure your course project, and only let the instructor listen!**

HearMyPaper is a cross-platform desktop application that lets students protect their academic work with military-grade cryptography. Submit your projects with confidence knowing only authorized instructors can access and listen to your submissions.

---

## ✨ Features

### 🔒 Military-Grade Security
- **End-to-end encryption** using industry-standard cryptographic algorithms
- Your work is encrypted locally before being submitted
- Only students and authorized instructors can decrypt submissions
- No plaintext data stored on servers

### 📁 Project Management
- Create and organize multiple projects
- Upload PDFs and documents for secure submission
- Track submission status and history
- View instructor feedback safely

### 🎯 Simple & Intuitive Interface
- Clean, modern desktop UI built with BeeWare Toga
- Drag-and-drop document upload
- One-click submission
- Real-time status updates

### 🔊 Audio Preview
- Convert your PDFs to audio for verification before submission
- Listen to how your work will sound to instructors
- Ensure document quality and completeness

### 📊 Submission Tracking
- View all submissions at a glance
- Check submission status and timestamps
- Manage multiple versions of your work
- Secure audit logs

---

## 📦 Supported Platforms

HearMyPaper runs on all major desktop operating systems:

| Platform | Status | Format |
|----------|--------|--------|
| **Windows** | ✅ Supported | `.msi` Installer |
| **Linux** (Ubuntu/Debian) | ✅ Supported | `.deb` Package |
| **Linux** (Arch) | ✅ Supported | Arch package |

### System Requirements

- **Minimum RAM**: 2 GB
- **Disk Space**: 500 MB
- **Internet**: Required for account authentication and submission
- **Python Runtime**: Built-in (no separate installation needed)

---

## 🚀 Installation

### Windows
1. Download the `.msi` installer from [HearMyPaper Releases](https://github.com/staleread/hearmypaper/releases)
2. Run the installer and follow the setup wizard
3. Launch HearMyPaper from your Start Menu

### Linux (Ubuntu/Debian)
```bash
sudo apt install ./hearmypaper_1.0.x_amd64.deb
hearmypaper  # Launch from terminal or application menu
```

### Linux (Arch)
```bash
sudo pacman -U hearmypaper-1.0.x-x86_64.pkg.tar.zst
hearmypaper  # Launch from application menu
```

---

## 🎓 Getting Started

1. **Create an Account**
   - Launch HearMyPaper
   - Click "Sign Up" and enter your student credentials
   - Verify your email address

2. **Set Up Your Project**
   - Navigate to "New Project"
   - Enter project name and description
   - Set submission deadline (optional)

3. **Upload Your Work**
   - Click "Add Files" or drag your PDF into the window
   - Review the document preview
   - Select "Upload" to begin encryption

4. **Verify Your Submission**
   - Use the audio preview feature to listen to your work
   - Make sure everything sounds correct
   - Submit when you're satisfied

5. **Track Status**
   - View all submissions in the "My Submissions" tab
   - Check instructor feedback when available
   - Re-submit updated versions as needed

---

## 🔐 Security & Privacy

- **Zero-Knowledge Architecture**: HearMyPaper never stores unencrypted data
- **End-to-End Encryption**: All data encrypted on your device before transmission
- **No Analytics**: We don't track your behavior or collect usage data
- **Open Source**: Code is auditable and transparent
- **Compliance**: Built with GDPR and data protection in mind

### Encryption Details
- Algorithm: AES-256-GCM (authenticated encryption)
- Key derivation: PBKDF2 with SHA-256
- Session tokens: JWT with HS256 signature

---

## 🆘 Support & Troubleshooting

### Application Won't Start
- Ensure you have Python 3.13+ installed (check installer system requirements)
- Try restarting your computer
- Reinstall the application if problem persists

### Can't Upload Files
- Check your internet connection
- Ensure file is in PDF format and under 100 MB
- Try uploading from a different network

### Forgot Your Password
- Click "Forgot Password?" on the login screen
- Follow the email verification process
- Set a new password

### Report a Bug
- Visit our [GitHub Issues](https://github.com/staleread/hearmypaper/issues)
- Include your OS version and steps to reproduce
- Attach error messages or screenshots

---

## 📱 Platform-Specific Notes

### Windows
- First launch may take a few seconds as the app initializes
- Windows Defender SmartScreen may show a warning (this is normal for unsigned apps)
- Requires .NET Framework 4.5+ (usually pre-installed)

### Linux
- GTK 3.0+ required (usually pre-installed)
- Some desktop environments may have different UI rendering

---

## 🌐 Learn More

- **Official Website**: [hearmypaper.io](https://staleread.github.io/HearMyPaper/)
- **Report Issues**: [GitHub Issues](https://github.com/staleread/hearmypaper/issues)

---

## 📄 License

HearMyPaper is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👥 Credits

**Developed by:**
- Mykola Ratushniak
- Neholiuk Oleksandr

**Built with:**
- [BeeWare Toga](https://beeware.org/) - Native GUI framework
- [Briefcase](https://briefcase.readthedocs.io/) - Cross-platform packaging
- [cryptography](https://cryptography.io/) - Encryption library

---

# 🛠️ Developer Guide

**This section is for developers who want to contribute to HearMyPaper.**

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager (recommended)
- Git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/staleread/hearmypaper.git
cd hearmypaper/client

# Create and activate virtual environment (optional, uv handles this)
python3.13 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies with uv
uv sync
```

### Run in Development Mode

```bash
# Start development server with hot reload
uv run briefcase dev

# Or with pip (if not using uv)
pip install -e ".[dev]"
briefcase dev
```

### Code Quality

```bash
# Lint with ruff
uv run ruff check .
uv run ruff check . --fix  # Auto-fix

# Type checking with mypy
uv run mypy .

# Run tests
uv run pytest
```

### Project Structure

```
client/
├── src/hearmypaper/          # Application source code
│   ├── app.py               # Main app entry point
│   ├── auth/                # Authentication
│   ├── submission/          # Submission management
│   ├── project/             # Project management
│   ├── shared/              # Shared utilities
│   └── resources/           # UI resources & config
├── tests/                   # Test suite
├── pyproject.toml          # Project metadata & dependencies
├── mypy.ini                # Type checking config
└── Dockerfile              # Container build (optional)
```

### Building for Release

```bash
# Build for current platform
uv run briefcase build

# Package for distribution
uv run briefcase package

# Build for specific platform (from any OS with Docker)
uv run briefcase package --target ubuntu:jammy   # Ubuntu DEB
uv run briefcase package --target arch:latest    # Arch Linux
uv run briefcase build windows                   # Windows (on Windows runner)
uv run briefcase build macOS                     # macOS (on macOS runner)
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes and run tests
4. Commit with clear messages
5. Push and create a Pull Request

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Version**: 1.0.4 | **Last Updated**: 2025-11-04
```

> [!NOTE]
> When running for the first time (or whenever the dependencies change)
> consider using `briefcase dev -r` to pack the required dependencies

---

## 📦 Building the App

BeeWare can package the app for multiple platforms:

* **Windows / macOS / Linux** (desktop)
* **iOS / Android** (mobile)

### Build & run a packaged app

```bash
briefcase create
briefcase build
briefcase run
```

### Make a distributable installer

```bash
briefcase package
```
