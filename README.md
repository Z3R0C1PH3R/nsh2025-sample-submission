# Space Station Cargo Management System - Hackathon Sample

This is a minimal sample implementation of the Space Station Cargo Management System API for the hackathon. It has been implemented in Python but you can use whatever you want.

## Getting Started

1. Clone this repository
2. Build the Docker container: `docker build -t cargo-management .`
3. Run the container: `docker run -p 8000:8000 cargo-management`
4. Test the API at http://localhost:8000

### Or you can try running the checker script with this repo's url: https://drive.google.com/file/d/1en9GyBDrRCPlaN073fiOiTjUTPjjaIst/view?usp=drive_link

## API Documentation

### Placement API
**Endpoint:** `POST /api/placement`

**Request:**
```json
{
  "items": [
    {
      "itemId": "item-1",
      "name": "Example Item",
      "width": 10,
      "depth": 10,
      "height": 10,
      "mass": 1,
      "priority": 1,
      "preferredZone": "A"
    }
  ],
  "containers": [
    {
      "containerId": "container-1",
      "zone": "A",
      "width": 100,
      "depth": 100,
      "height": 100
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "placements": [
    {
      "itemId": "item-1",
      "containerId": "container-1",
      "position": {
        "startCoordinates": {"width": 0, "depth": 0, "height": 0},
        "endCoordinates": {"width": 10, "depth": 10, "height": 10}
      }
    }
  ]
}
```

## Required Features

Your solution should implement all the APIs described in the problem statement:

1. ✅ Placement API (Sample provided. Use your own code instead.)
2. 📝 Search API
3. 📝 Retrieve API
4. 📝 Place API
5. 📝 Waste Management APIs
6. 📝 Time Simulation API
7. 📝 Import/Export APIs
8. 📝 Logging API

Good luck!
