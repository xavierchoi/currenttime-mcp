# CurrentTime MCP Server 🕐

**[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md)**

[![PyPI version](https://badge.fury.io/py/currenttime-mcp.svg)](https://pypi.org/project/currenttime-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

IP ベースのタイムゾーン検出により正確な現在時刻を提供する MCP（Model Context Protocol）サーバーです。

Claude Code、Cursor、その他の MCP 対応エディターで**「今何時？」**と聞くと、自動的にあなたの位置を検出して正確な時刻をお知らせします！⚡

## 機能

- **自動タイムゾーン検出**: クライアントのIPアドレスに基づいてタイムゾーンを自動検出
- **正確な時刻提供**: pytzライブラリを使用して正確な現在時刻を計算
- **多様なタイムゾーン対応**: 世界597のタイムゾーンをサポート
- **クライアント情報**: IPベースの位置情報とタイムゾーン情報を提供

## 提供されるツール

### 1. `get_current_time`
クライアントのIPに基づいてタイムゾーンを自動検出し、現在時刻を返します。

**パラメータ:**
- `client_ip` (オプション): 特定のIPアドレスを指定できます。

**戻り値:**
- `current_time`: ISO形式の現在時刻
- `timezone`: 検出されたタイムゾーン（例: "Asia/Seoul"）
- `formatted_time`: 読みやすい形式の時刻（例: "2025-08-27 21:55:40 KST"）
- `location`: 都市、地域、国の情報
- `utc_offset`: UTC オフセット
- `is_dst`: 夏時間適用状況

### 2. `get_time_for_timezone`
特定のタイムゾーンの現在時刻を返します。

**パラメータ:**
- `timezone_name`: タイムゾーン名（例: "America/New_York", "Europe/London"）

### 3. `get_client_info`
クライアントのIPベースの位置情報とタイムゾーンを返します。

**パラメータ:**
- `client_ip` (オプション): 特定のIPアドレスを指定できます。

### 4. `list_common_timezones`
地域別に整理された一般的なタイムゾーンのリストを返します。

## クイックインストール（推奨）⚡

Claude Code で一行でインストールできます：

```bash
claude mcp add currenttime --scope user -- uvx currenttime-mcp
```

インストール後、Claude Code を再起動すれば使用可能です！🚀

## 手動インストール

### 1. PyPI からインストール

```bash
# uvx で即座に実行（インストール不要、推奨）
uvx currenttime-mcp

# または uv tool でインストール
uv tool install currenttime-mcp

# または pip を使用
pip install currenttime-mcp
```

### 2. Claude Code 設定

Claude Code の `config.toml` ファイルに以下を追加してください：

```toml
[mcp_servers.currenttime]
command = "uvx"
args = ["currenttime-mcp"]

# または pip でインストールした場合
[mcp_servers.currenttime]  
command = "currenttime-mcp"
```

### 3. テスト

```bash
# 機能テスト
source venv/bin/activate
python test_server.py
```

## 使用例

Claude Code で自然言語リクエストができます：

- 💬 「今何時？」
- 🌍 「ニューヨークの現在時刻を教えて」
- 📍 「私のタイムゾーン情報を表示して」
- 🕐 「利用可能なタイムゾーンを表示して」

### 実際の応答例
```
🕘 現在時刻: 2025年8月27日 午後11時26分5秒（KST）
📍 位置: 城北区, ソウル, 韓国 🇰🇷
⏰ タイムゾーン: Asia/Seoul（UTC+9）
```

## API 情報

この MCP サーバーは以下の外部サービスを使用します：
- **ipapi.co**: IP ベースの地理的位置およびタイムゾーン検出（月間30,000リクエスト無料）

環境変数で設定を調整できます：
- `IPAPI_BASE`: デフォルト API エンドポイント（デフォルト: `https://ipapi.co`）
- `IPAPI_KEY`: ipapi プレミアム/個人キー（利用可能な場合クォータ増加）

## 技術スタック

- **Python 3.8+**
- **MCP (Model Context Protocol)**: AI モデルとの標準化された通信
- **FastMCP**: MCP サーバー実装のためのハイレベルフレームワーク
- **requests**: HTTP クライアント
- **pytz**: タイムゾーン処理

## ライセンス

このプロジェクトは MIT ライセンスの下で提供されています。