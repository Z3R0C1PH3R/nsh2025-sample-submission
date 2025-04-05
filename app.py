from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
containers = {}
items = {}

# Root endpoint
@app.route('/')
def index():
    return "Space Station Cargo Management System API"

# Placement API
@app.route('/api/placement', methods=['POST'])
def placement():
    data = request.json
    new_items = data.get('items', [])
    available_containers = data.get('containers', [])
    
    # Store containers and items
    for container in available_containers:
        containers[container['containerId']] = container
    
    for item in new_items:
        items[item['itemId']] = item
    
    # Simple placement logic
    placements = []
    
    for item in new_items:
        item_id = item['itemId']
        preferred_zone = item.get('preferredZone')
        
        # Find a suitable container in preferred zone
        suitable_container = None
        for container_id, container in containers.items():
            if container['zone'] == preferred_zone:
                suitable_container = container
                break
        
        if suitable_container:
            # Place item at position 0,0,0 for simplicity
            placement = {
                "itemId": item_id,
                "containerId": suitable_container['containerId'],
                "position": {
                    "startCoordinates": {"width": 0, "depth": 0, "height": 0},
                    "endCoordinates": {
                        "width": item['width'],
                        "depth": item['depth'],
                        "height": item['height']
                    }
                }
            }
            placements.append(placement)
            
            # Update item location
            items[item_id]['containerId'] = suitable_container['containerId']
            items[item_id]['position'] = placement['position']
    
    return jsonify({
        "success": True,
        "placements": placements
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
