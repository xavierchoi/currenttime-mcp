#!/usr/bin/env python3
"""
CurrentTime MCP Server
Provides accurate current time with IP-based timezone detection
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Any, Dict, Optional

import pytz
import requests
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the MCP server
mcp = FastMCP("CurrentTime")


@mcp.tool()
def get_current_time(client_ip: Optional[str] = None) -> Dict[str, Any]:
    """
    Get the current time with automatic timezone detection based on IP address.
    
    Args:
        client_ip: Optional IP address. If not provided, will detect automatically.
        
    Returns:
        Dictionary containing current time, timezone, and location info
    """
    try:
        # Get timezone info from IP
        if client_ip:
            url = f"https://ipapi.co/{client_ip}/json/"
        else:
            url = "https://ipapi.co/json/"
            
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        location_data = response.json()
        
        # Extract timezone
        timezone_name = location_data.get('timezone', 'UTC')
        
        # Get current time in the detected timezone
        tz = pytz.timezone(timezone_name)
        current_time = datetime.now(tz)
        
        return {
            "success": True,
            "current_time": current_time.isoformat(),
            "timezone": timezone_name,
            "utc_offset": current_time.strftime("%z"),
            "formatted_time": current_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "timestamp": current_time.timestamp(),
            "location": {
                "city": location_data.get('city'),
                "region": location_data.get('region'),
                "country": location_data.get('country_name'),
                "country_code": location_data.get('country_code'),
                "ip": location_data.get('ip')
            },
            "is_dst": bool(current_time.dst())
        }
        
    except requests.RequestException as e:
        logger.error(f"Network error: {e}")
        # Fallback to UTC time
        utc_time = datetime.now(pytz.UTC)
        return {
            "success": False,
            "error": "Could not detect timezone, using UTC",
            "current_time": utc_time.isoformat(),
            "timezone": "UTC",
            "utc_offset": "+0000",
            "formatted_time": utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "timestamp": utc_time.timestamp()
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            "success": False,
            "error": str(e),
            "current_time": None
        }


@mcp.tool()
def get_time_for_timezone(timezone_name: str) -> Dict[str, Any]:
    """
    Get the current time for a specific timezone.
    
    Args:
        timezone_name: Timezone name (e.g., 'America/New_York', 'Asia/Seoul', 'Europe/London')
        
    Returns:
        Dictionary containing current time for the specified timezone
    """
    try:
        # Validate timezone
        tz = pytz.timezone(timezone_name)
        current_time = datetime.now(tz)
        
        return {
            "success": True,
            "current_time": current_time.isoformat(),
            "timezone": timezone_name,
            "utc_offset": current_time.strftime("%z"),
            "formatted_time": current_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "timestamp": current_time.timestamp(),
            "is_dst": bool(current_time.dst())
        }
        
    except pytz.UnknownTimeZoneError:
        return {
            "success": False,
            "error": f"Unknown timezone: {timezone_name}",
            "available_timezones": "Use pytz.all_timezones to see available timezones"
        }
        
    except Exception as e:
        logger.error(f"Error getting time for timezone {timezone_name}: {e}")
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
def get_client_info(client_ip: Optional[str] = None) -> Dict[str, Any]:
    """
    Get client location and timezone information based on IP address.
    
    Args:
        client_ip: Optional IP address. If not provided, will detect automatically.
        
    Returns:
        Dictionary containing client location and timezone info
    """
    try:
        # Get location info from IP
        if client_ip:
            url = f"https://ipapi.co/{client_ip}/json/"
        else:
            url = "https://ipapi.co/json/"
            
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        return {
            "success": True,
            "ip": data.get('ip'),
            "city": data.get('city'),
            "region": data.get('region'),
            "country": data.get('country_name'),
            "country_code": data.get('country_code'),
            "timezone": data.get('timezone'),
            "latitude": data.get('latitude'),
            "longitude": data.get('longitude'),
            "postal": data.get('postal'),
            "calling_code": data.get('calling_code'),
            "currency": data.get('currency'),
            "languages": data.get('languages'),
            "asn": data.get('asn'),
            "org": data.get('org')
        }
        
    except requests.RequestException as e:
        logger.error(f"Network error: {e}")
        return {
            "success": False,
            "error": "Could not retrieve client information",
            "details": str(e)
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
def list_common_timezones() -> Dict[str, Any]:
    """
    Get a list of common timezones grouped by region.
    
    Returns:
        Dictionary containing common timezones organized by region
    """
    common_timezones = {
        "America": [
            "America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles",
            "America/Toronto", "America/Vancouver", "America/Mexico_City", "America/Sao_Paulo",
            "America/Buenos_Aires", "America/Lima", "America/Bogota"
        ],
        "Europe": [
            "Europe/London", "Europe/Paris", "Europe/Berlin", "Europe/Rome", 
            "Europe/Madrid", "Europe/Amsterdam", "Europe/Stockholm", "Europe/Moscow",
            "Europe/Istanbul", "Europe/Athens"
        ],
        "Asia": [
            "Asia/Tokyo", "Asia/Seoul", "Asia/Shanghai", "Asia/Hong_Kong",
            "Asia/Singapore", "Asia/Bangkok", "Asia/Mumbai", "Asia/Dubai",
            "Asia/Jakarta", "Asia/Manila"
        ],
        "Australia": [
            "Australia/Sydney", "Australia/Melbourne", "Australia/Perth", "Australia/Brisbane",
            "Australia/Adelaide", "Australia/Darwin"
        ],
        "Africa": [
            "Africa/Cairo", "Africa/Lagos", "Africa/Johannesburg", "Africa/Nairobi",
            "Africa/Casablanca", "Africa/Tunis"
        ],
        "UTC": ["UTC"]
    }
    
    return {
        "success": True,
        "common_timezones": common_timezones,
        "total_available": len(pytz.all_timezones),
        "note": "Use get_time_for_timezone() with any of these timezone names"
    }


def main():
    """Main entry point for the MCP server."""
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


if __name__ == "__main__":
    main()