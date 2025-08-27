#!/usr/bin/env python3
"""
Test script for CurrentTime MCP Server
"""

import sys
sys.path.append('/Users/internetbasedboy/currenttime-mcp')

from currenttime_mcp.server import get_current_time, get_time_for_timezone, get_client_info, list_common_timezones

def test_get_current_time():
    print("=== Testing get_current_time ===")
    result = get_current_time()
    print(f"Success: {result.get('success')}")
    if result.get('success'):
        print(f"Current time: {result.get('formatted_time')}")
        print(f"Timezone: {result.get('timezone')}")
        print(f"Location: {result.get('location', {}).get('city')}, {result.get('location', {}).get('country')}")
    else:
        print(f"Error: {result.get('error')}")
    print()

def test_get_time_for_timezone():
    print("=== Testing get_time_for_timezone ===")
    timezones = ['Asia/Seoul', 'America/New_York', 'Europe/London', 'UTC']
    for tz in timezones:
        result = get_time_for_timezone(tz)
        print(f"Timezone {tz}: {result.get('formatted_time') if result.get('success') else result.get('error')}")
    print()

def test_get_client_info():
    print("=== Testing get_client_info ===")
    result = get_client_info()
    print(f"Success: {result.get('success')}")
    if result.get('success'):
        print(f"IP: {result.get('ip')}")
        print(f"Location: {result.get('city')}, {result.get('country')}")
        print(f"Timezone: {result.get('timezone')}")
    else:
        print(f"Error: {result.get('error')}")
    print()

def test_list_common_timezones():
    print("=== Testing list_common_timezones ===")
    result = list_common_timezones()
    print(f"Success: {result.get('success')}")
    if result.get('success'):
        print(f"Total available timezones: {result.get('total_available')}")
        print("Sample timezones by region:")
        for region, zones in result.get('common_timezones', {}).items():
            print(f"  {region}: {zones[:3]}...")  # Show first 3 timezones
    print()

if __name__ == "__main__":
    print("Testing CurrentTime MCP Server Functions")
    print("=" * 50)
    
    test_get_current_time()
    test_get_time_for_timezone()
    test_get_client_info()
    test_list_common_timezones()
    
    print("All tests completed!")