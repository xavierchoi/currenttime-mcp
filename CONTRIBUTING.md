# Contributing to CurrentTime MCP Server

Thank you for your interest in contributing to CurrentTime MCP Server! This document provides guidelines for contributing to this project.

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork**: `git clone https://github.com/your-username/currenttime-mcp.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes**
5. **Test your changes**
6. **Submit a Pull Request**

## 🛠 Development Setup

### Prerequisites
- Python 3.8 or higher
- `uv` or `pip` for package management

### Local Development
```bash
# Clone the repository
git clone https://github.com/xavierchoi/currenttime-mcp.git
cd currenttime-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Run tests
python test_server.py

# Test the MCP server
uvx currenttime-mcp
```

## 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior**
- **Actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Error messages** (if any)

## 💡 Suggesting Features

Feature suggestions are welcome! Please:

1. **Check existing issues** for similar suggestions
2. **Describe the feature** clearly
3. **Explain the use case** and benefits
4. **Consider implementation** complexity

## 🔧 Code Contributions

### Code Style
- Follow **PEP 8** Python style guidelines
- Use **descriptive variable names**
- Add **docstrings** for functions and classes
- Keep **functions focused** and small
- Add **type hints** where appropriate

### Testing
- **Test your changes** thoroughly
- Run `python test_server.py` before submitting
- Add tests for new features
- Ensure existing tests still pass

### Commit Messages
Use clear, descriptive commit messages:
```
Add timezone caching functionality

- Implement TTL cache for IP->timezone lookups
- Reduce API calls to ipapi.co
- Add cache configuration via environment variables
- Update documentation with cache settings
```

## 📝 Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update README.md** if necessary
5. **Create a clear PR description**

### PR Description Template
```markdown
## Summary
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please specify)

## Testing
- [ ] Tested locally
- [ ] Added/updated tests
- [ ] All existing tests pass

## Screenshots (if applicable)
```

## 🏗 Architecture Guidelines

### File Structure
```
currenttime-mcp/
├── currenttime_mcp/
│   ├── __init__.py          # Package metadata
│   └── server.py            # Main MCP server logic
├── tests/                   # Test files (future)
├── docs/                    # Documentation (future)
└── examples/                # Usage examples (future)
```

### Adding New Features

#### New MCP Tools
When adding new tools to the MCP server:

1. **Add the function** in `currenttime_mcp/server.py`
2. **Use `@mcp.tool()` decorator**
3. **Include comprehensive docstrings**
4. **Handle errors gracefully**
5. **Return structured responses**

Example:
```python
@mcp.tool()
def get_timezone_info(timezone_name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific timezone.
    
    Args:
        timezone_name: Name of the timezone (e.g., 'America/New_York')
        
    Returns:
        Dictionary containing timezone details
    """
    try:
        # Implementation here
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

#### External API Integration
- **Use the existing session** (`_session`) for HTTP requests
- **Implement proper error handling**
- **Add timeout configurations**
- **Consider rate limiting**
- **Support environment variable configuration**

## 🔒 Security Considerations

- **Validate all inputs**, especially IP addresses
- **Sanitize API responses** before processing
- **Avoid logging sensitive information**
- **Use HTTPS for external API calls**
- **Handle authentication securely**

## 🌐 Internationalization

- **Use English** for code comments and documentation
- **Support UTF-8** encoding
- **Consider time format** preferences
- **Handle different date formats**

## 📚 Documentation

- **Update README.md** for new features
- **Add inline code comments** for complex logic
- **Include usage examples**
- **Document environment variables**
- **Update API documentation**

## 🤝 Community Guidelines

- **Be respectful** and inclusive
- **Help newcomers** get started
- **Share knowledge** and best practices
- **Give constructive feedback**
- **Follow the Code of Conduct**

## 🏷 Release Process

For maintainers:

1. **Update version** in `pyproject.toml` and `__init__.py`
2. **Update CHANGELOG.md**
3. **Create release notes**
4. **Tag the release**
5. **Build and publish** to PyPI
6. **Update documentation**

## 💬 Getting Help

- **Create an issue** for questions
- **Check existing issues** first
- **Be specific** about your problem
- **Provide context** and examples

## 🎯 Good First Issues

Looking for ways to contribute? Check for issues labeled:
- `good first issue`
- `help wanted`
- `documentation`
- `enhancement`

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to CurrentTime MCP Server! Your help makes this project better for everyone. 🚀