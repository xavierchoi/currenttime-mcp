# CurrentTime MCP Server 🕐

**[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md)**

[![PyPI version](https://badge.fury.io/py/currenttime-mcp.svg)](https://pypi.org/project/currenttime-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An MCP (Model Context Protocol) server that provides accurate current time with IP-based timezone detection.

When you ask **"What time is it now?"** in Claude Code, Cursor, or other MCP-compatible editors, it automatically detects your location and tells you the exact time! ⚡

## Features

- **Automatic Timezone Detection**: Automatically detects timezone based on client's IP address
- **Accurate Time Provision**: Calculates precise current time using the pytz library
- **Multiple Timezone Support**: Supports 597 timezones worldwide
- **Client Information**: Provides IP-based location information and timezone details

## Available Tools

### 1. `get_current_time`
Automatically detects timezone based on client's IP and returns the current time.

**Parameters:**
- `client_ip` (optional): You can specify a specific IP address.

**Returns:**
- `current_time`: Current time in ISO format
- `timezone`: Detected timezone (e.g., "Asia/Seoul")
- `formatted_time`: Human-readable time format (e.g., "2025-08-27 21:55:40 KST")
- `location`: City, region, country information
- `utc_offset`: UTC offset
- `is_dst`: Daylight saving time status

### 2. `get_time_for_timezone`
Returns the current time for a specific timezone.

**Parameters:**
- `timezone_name`: Timezone name (e.g., "America/New_York", "Europe/London")

### 3. `get_client_info`
Returns client's IP-based location information and timezone.

**Parameters:**
- `client_ip` (optional): You can specify a specific IP address.

### 4. `list_common_timezones`
Returns a list of common timezones organized by region.

## Quick Installation (Recommended) ⚡

Install with one line in Claude Code:

```bash
claude mcp add currenttime --scope user -- uvx currenttime-mcp
```

Restart Claude Code after installation and it's ready to use! 🚀

## Manual Installation

### 1. Install from PyPI

```bash
# Run instantly with uvx (no installation required, recommended)
uvx currenttime-mcp

# Or install with uv tool
uv tool install currenttime-mcp

# Or use pip
pip install currenttime-mcp
```

### 2. Claude Code Configuration

Add the following to your `config.toml` file in Claude Code:

```toml
[mcp_servers.currenttime]
command = "uvx"
args = ["currenttime-mcp"]

# Or if installed with pip
[mcp_servers.currenttime]  
command = "currenttime-mcp"
```

### 3. Testing

```bash
# Function testing
source venv/bin/activate
python test_server.py
```

## Usage Examples

You can make natural language requests in Claude Code:

- 💬 "What time is it now?"
- 🌍 "What time is it in New York?"
- 📍 "Show me my timezone information"  
- 🕐 "Show me available timezones"

### Actual Response Example
```
🕘 Current Time: August 27, 2025, 11:26:05 PM (KST)
📍 Location: Seongbuk-gu, Seoul, South Korea 🇰🇷
⏰ Timezone: Asia/Seoul (UTC+9)
```

## API Information

This MCP server uses the following external services:
- **ipapi.co**: IP-based geographic location and timezone detection (30,000 requests/month free)

You can adjust settings with environment variables:
- `IPAPI_BASE`: Default API endpoint (default: `https://ipapi.co`)
- `IPAPI_KEY`: ipapi premium/personal key (increases quota if available)

## Tech Stack

- **Python 3.8+**
- **MCP (Model Context Protocol)**: Standardized communication with AI models
- **FastMCP**: High-level framework for MCP server implementation
- **requests**: HTTP client
- **pytz**: Timezone handling

## License

This project is licensed under the MIT License.