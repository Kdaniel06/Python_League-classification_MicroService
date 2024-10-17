# League table classification Microservice

This microservice is built with FastAPI and allows you to manage the classification of teams in different zones based on their points and goal difference.

## Requirements

- Python 3.7 or higher
- FastAPI
- Pydantic
- Pytest

## Installation

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
    * On Windows:
        ```bash
        venv\Scripts\activate
        ```
    
    * On macOS/Linux:
        ```bash
        source venv/bin/activate 
        ```

3. **Install FastAPI and Uvicorn:**
    ```bash
    pip install fastapi uvicorn
    ```

4. **Running the Server**
    To run the server, use the following command:
        ```bash
        uvicorn main:app --reload
        ```

This will start the server at http://127.0.0.1:8000.

## Endpoints
### 1. Get Team Positions
    
**Endpoint**: /positions/
**Method**: POST
**Description**: This endpoint receives a list of teams and returns the sorted list based on points and goal difference.

#### Example Request:
    
```json
[
    {"name": "TEAM A", "zone": "ZONE A", "difference": 10, "points": 25},
    {"name": "TEAM B", "zone": "ZONE A", "difference": 5, "points": 22},
    {"name": "TEAM C", "zone": "ZONE A", "difference": -2, "points": 15},
    
    {"name": "TEAM D", "zone": "ZONE B", "difference": 8, "points": 22},
    {"name": "TEAM E", "zone": "ZONE B", "difference": 3, "points": 12},
    {"name": "TEAM F", "zone": "ZONE B", "difference": -1, "points": 12},
    
    {"name": "TEAM G", "zone": "ZONE C", "difference": 15, "points": 30},
    {"name": "TEAM H", "zone": "ZONE C", "difference": 7, "points": 19},
    {"name": "TEAM I", "zone": "ZONE C", "difference": -3, "points": 14},
    
    {"name": "TEAM J", "zone": "ZONE D", "difference": 6, "points": 21},
    {"name": "TEAM K", "zone": "ZONE D", "difference": -4, "points": 10},
    {"name": "TEAM L", "zone": "ZONE D", "difference": -8, "points": 8}
]
```

#### Example Response
```json
[
    {"name": "TEAM G", "zone": "ZONE C", "difference": 15, "points": 30},
    {"name": "TEAM A", "zone": "ZONE A", "difference": 10, "points": 25},
    {"name": "TEAM J", "zone": "ZONE D", "difference": 6, "points": 21},
    {"name": ...}
]
```
    
### 2. Get Positions by Zone

**Endpoint**: /positions_by_zone/
**Method**: POST
**Description**: This endpoint receives a list of teams and returns the teams grouped by zone and sorted by points and goal difference.

#### Example Request
```json
[
    {"name": "TEAM A", "zone": "ZONE A", "difference": 10, "points": 25},
    {"name": "TEAM B", "zone": "ZONE A", "difference": 5, "points": 22},
    {"name": "TEAM C", "zone": "ZONE A", "difference": -2, "points": 15},
    
    {"name": "TEAM D", "zone": "ZONE B", "difference": 8, "points": 22},
    {"name": "TEAM E", "zone": "ZONE B", "difference": 3, "points": 12},
    {"name": "TEAM F", "zone": "ZONE B", "difference": -1, "points": 12},
    
    {"name": "TEAM G", "zone": "ZONE C", "difference": 15, "points": 30},
    {"name": "TEAM H", "zone": "ZONE C", "difference": 7, "points": 19},
    {"name": "TEAM I", "zone": "ZONE C", "difference": -3, "points": 14},
    
    {"name": "TEAM J", "zone": "ZONE D", "difference": 6, "points": 21},
    {"name": "TEAM K", "zone": "ZONE D", "difference": -4, "points": 10},
    {"name": "TEAM L", "zone": "ZONE D", "difference": -8, "points": 8}
]
```

#### Example Response
```json
{
    "ZONE A": [
        {
            "name": "TEAM A",
            "zone": "ZONE A",
            "difference": 10,
            "points": 25
        },
        {
            ...
        }
    ],
    "ZONE B": [
        {
            "name": "TEAM D",
            "zone": "ZONE B",
            "difference": 8,
            "points": 22
        },
        {
            ...
        }
    ]
    ...
}
```

### Automatic testing
If you want to test the endpoints you can use **PyTest**. Install pytest in your environment and run the code:
```bash
   pytest
```

After run the command you will be able to see the passed and failed tests. Yoou can go to the *testing_jsons.py* file and change the requests to test the endpoints in different situations.

## Contributions
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.
