from flask import Flask, render_template, request, jsonify
from directed_graph import DirectedGraph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    edge_list = data.get('edges', '')
    start_node = data.get('start', '').strip()
    target_node = data.get('target', '').strip()

    g = DirectedGraph()
    
    # Parse edges
    lines = edge_list.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 3:
            u = parts[0].strip()
            v = parts[1].strip()
            try:
                d = float(parts[2].strip())
                g.add_edge(u, v, d)
            except ValueError:
                continue # Skip invalid lines

    # Calculate shortest path
    if start_node and target_node:
        try:
            g.dijkstra(start_node)
            path, cost = g.get_shortest_path(target_node)
            graph_data = g.get_graph_data()
            
            return jsonify({
                "nodes": graph_data['nodes'],
                "edges": graph_data['edges'],
                "path": path,
                "path_cost": cost,
                "error": None
            })
        except Exception as e:
             return jsonify({"error": str(e)}), 400
    
    return jsonify({"error": "Missing start or target node"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
