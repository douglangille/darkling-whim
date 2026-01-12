# Apple Ecosystem AI Extensions
*MCP servers for Gemini CLI + Apple integrations*

## Apple Notes MCP
**Server:** `apple-notes-mcp`
**Repository:** github.com/disco-trooper/apple-notes-mcp

### Installation
```bash
git clone https://github.com/disco-trooper/apple-notes-mcp
cd apple-notes-mcp
bun install  # or npm install
```

### Configuration
Add to `~/.gemini/settings.json`:
```json
{
  "mcpServers": {
    "apple-notes": {
      "command": "node",
      "args": ["/path/to/apple-notes-mcp/server"]
    }
  }
}
```

### Usage
```
gemini> @apple-notes search story ideas
gemini> @apple-notes create note from batch analysis
```

## Apple Reminders MCP
**Server:** `mcp-server-apple-reminders`

### Installation
```bash
npm i -g mcp-server-apple-reminders
# Requires Xcode CLI tools
