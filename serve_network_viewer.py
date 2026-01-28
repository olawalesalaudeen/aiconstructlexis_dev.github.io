#!/usr/bin/env python3
"""
Simple HTTP server to serve the network viewer HTML page.

Usage:
    python visualize_networks/serve_network_viewer.py --port 8000
    cd visualize_networks && python serve_network_viewer.py --port 8000
"""

import argparse
import http.server
import socketserver
import os
import json
from pathlib import Path


class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS headers."""
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        """Suppress log messages for cleaner output."""
        pass

    def do_GET(self):
        """Handle GET requests, including API endpoints."""
        # API endpoint to list aggregated network files
        if self.path == '/api/list-files' or self.path.startswith('/api/list-files'):
            try:
                # Use current working directory (set in main())
                aggregated_dir = Path('aggregated_networks')
                cwd = Path.cwd()
                
                files = []
                if aggregated_dir.exists():
                    for file_path in sorted(aggregated_dir.glob('*.json')):
                        # Skip embedding cache files
                        if 'embeddings_cache' not in file_path.name:
                            files.append(file_path.name)
                    print(f"API: Found {len(files)} files in {aggregated_dir.resolve()}")
                else:
                    print(f"API Warning: aggregated_networks directory not found at {aggregated_dir.resolve()}")
                    print(f"Current working directory: {cwd}")
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(files).encode())
                return
            except Exception as e:
                print(f"API Error: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
                return
        
        # Serve normal files
        super().do_GET()


def main():
    parser = argparse.ArgumentParser(description='Serve the network viewer')
    parser.add_argument(
        '--port', 
        type=int, 
        default=8000, 
        help='Port to serve on (default: 8000)'
    )
    parser.add_argument(
        '--directory',
        type=str,
        default=None,
        help='Directory to serve from (default: project root)'
    )
    
    args = parser.parse_args()
    
    # Default to project root (parent of visualize_networks)
    if args.directory is None:
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        os.chdir(project_root)
        directory = str(project_root)
    else:
        directory = args.directory
        os.chdir(directory)
    
    PORT = args.port
    
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print(f"🌐 Server started at http://localhost:{PORT}")
        print(f"📁 Serving from: {directory}")
        print(f"📋 Open http://localhost:{PORT}/visualize_networks/view_network.html in your browser")
        print(f"🛑 Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == "__main__":
    main()

