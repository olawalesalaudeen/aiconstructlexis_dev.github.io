# Nomological Network Visualizer

Interactive web-based explorer for aggregated nomological networks.

## Features

- **Search**: Search constructs, measurements, and behaviors by name or definition
- **Filter**: Filter by type (Constructs, Measurements, Behaviors)
- **Visualization**: Interactive network graph showing relationships
- **Details**: View all relationships (incoming and outgoing) for any node

## Usage

### Option 1: Run the server script

```bash
cd visualize_networks
python serve_network_viewer.py --port 8000
```

Then open http://localhost:8000/view_network.html in your browser.

### Option 2: Open directly in browser

You can also open `view_network.html` directly in your browser, but note that:
- Some browsers may block local file access for security reasons
- Loading large JSON files directly may be slower

## How to Use

1. **Load JSON**: Click "Load JSON" and select your aggregated network file (e.g., `aggregated_networks/neurips_2024_aggregated_smart_v3.json`)

2. **Search**: Type in the search box to filter nodes by name or definition text

3. **Filter**: Click filter buttons to show only specific types (Constructs, Measurements, Behaviors)

4. **Select Node**: Click on any node in the search results to:
   - See it highlighted in the network graph
   - View all connected nodes
   - See detailed relationship information in the bottom panel

5. **Interact with Graph**: 
   - Click on nodes in the graph to select them
   - Drag nodes to rearrange
   - Zoom and pan to explore
   - Click "Reset View" to recenter

## File Structure

- `view_network.html`: Main interactive viewer (uses vis.js for network visualization)
- `serve_network_viewer.py`: Simple HTTP server to serve the HTML file
- `README.md`: This file

## Requirements

No Python dependencies needed for the HTML file itself. The server script uses only standard library.

The viewer uses:
- [vis-network](https://visjs.github.io/vis-network/) (loaded from CDN) for graph visualization

