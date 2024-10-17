# * All the JSON files that the app needs to be tested

# ? The request 
testingTeams = [
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

# ? Sort all the teams together response
sorted_all_together = [
    {
        "name": "TEAM G",
        "zone": "ZONE C",
        "difference": 15,
        "points": 30
    },
    {
        "name": "TEAM A",
        "zone": "ZONE A",
        "difference": 10,
        "points": 25
    },
    {
        "name": "TEAM D",
        "zone": "ZONE B",
        "difference": 8,
        "points": 22
    },
    {
        "name": "TEAM B",
        "zone": "ZONE A",
        "difference": 5,
        "points": 22
    },
    {
        "name": "TEAM J",
        "zone": "ZONE D",
        "difference": 6,
        "points": 21
    },
    {
        "name": "TEAM H",
        "zone": "ZONE C",
        "difference": 7,
        "points": 19
    },
    {
        "name": "TEAM C",
        "zone": "ZONE A",
        "difference": -2,
        "points": 15
    },
    {
        "name": "TEAM I",
        "zone": "ZONE C",
        "difference": -3,
        "points": 14
    },
    {
        "name": "TEAM E",
        "zone": "ZONE B",
        "difference": 3,
        "points": 12
    },
    {
        "name": "TEAM F",
        "zone": "ZONE B",
        "difference": -1,
        "points": 12
    },
    {
        "name": "TEAM K",
        "zone": "ZONE D",
        "difference": -4,
        "points": 10
    },
    {
        "name": "TEAM L",
        "zone": "ZONE D",
        "difference": -8,
        "points": 8
    }
]

# ? Sort all the teams by zone response
sorted_by_zone = {
    "ZONE A": [
        {
            "name": "TEAM A",
            "zone": "ZONE A",
            "difference": 10,
            "points": 25
        },
        {
            "name": "TEAM B",
            "zone": "ZONE A",
            "difference": 5,
            "points": 22
        },
        {
            "name": "TEAM C",
            "zone": "ZONE A",
            "difference": -2,
            "points": 15
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
            "name": "TEAM E",
            "zone": "ZONE B",
            "difference": 3,
            "points": 12
        },
        {
            "name": "TEAM F",
            "zone": "ZONE B",
            "difference": -1,
            "points": 12
        }
    ],
    "ZONE C": [
        {
            "name": "TEAM G",
            "zone": "ZONE C",
            "difference": 15,
            "points": 30
        },
        {
            "name": "TEAM H",
            "zone": "ZONE C",
            "difference": 7,
            "points": 19
        },
        {
            "name": "TEAM I",
            "zone": "ZONE C",
            "difference": -3,
            "points": 14
        }
    ],
    "ZONE D": [
        {
            "name": "TEAM J",
            "zone": "ZONE D",
            "difference": 6,
            "points": 21
        },
        {
            "name": "TEAM K",
            "zone": "ZONE D",
            "difference": -4,
            "points": 10
        },
        {
            "name": "TEAM L",
            "zone": "ZONE D",
            "difference": -8,
            "points": 8
        }
    ]
}