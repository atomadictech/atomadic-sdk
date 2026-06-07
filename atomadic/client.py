"""Atomadic MCP client -- thin JSON-RPC wrapper over mcp.atomadic.tech."""
import os, json, urllib.request

DEFAULT_URL = 'https://mcp.atomadic.tech'

class Atomadic:
    '''Thin MCP client. Set api_key explicitly or via ATOMADIC_KEY env var.'''
    def __init__(self, api_key=None, url=None):
        self.api_key = api_key or os.environ.get('ATOMADIC_KEY', '')
        self.url = url or os.environ.get('ATOMADIC_MCP_URL', DEFAULT_URL)
        self._id = 0
    def _rpc(self, method, params):
        self._id += 1
        body = json.dumps({'jsonrpc': '2.0', 'id': self._id, 'method': method, 'params': params}).encode('utf-8')
        req = urllib.request.Request(self.url, data=body, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + (self.api_key or '')})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode('utf-8'))
    def call(self, tool, arguments=None):
        resp = self._rpc('tools/call', {'name': tool, 'arguments': arguments or {}})
        if 'error' in resp:
            raise RuntimeError('MCP error: ' + json.dumps(resp['error']))
        content = (resp.get('result') or {}).get('content') or []
        if content and content[0].get('type') == 'text':
            text = content[0].get('text', '')
            try:
                return json.loads(text)
            except (ValueError, TypeError):
                return text
        return resp.get('result')
    def list_tools(self):
        return (self._rpc('tools/list', {}).get('result') or {}).get('tools', [])
