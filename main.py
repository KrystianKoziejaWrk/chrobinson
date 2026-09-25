from fastapi import FastAPI
from collections import deque



#web server
app = FastAPI()


graph = {
    "CAN": ["USA"],
    "USA": ["CAN", "MEX"],
    "MEX": ["USA", "GTM", "BLZ"],
    "BLZ": ["MEX", "GTM"],
    "GTM": ["MEX", "BLZ", "SLV", "HND"],
    "SLV": ["GTM", "HND"],
    "HND": ["GTM", "SLV", "NIC"],
    "NIC": ["HND", "CRI"],
    "CRI": ["NIC", "PAN"],
    "PAN": ["CRI"]
}


#algoritm 
#https://www.redblobgames.com/pathfinding/a-star/introduction.html

def bfs(graph, start):
    q = deque()
    q.append(start)
    distances = {start:0}
    prev = {}   
    while q:
        current = q.popleft()

        for neighbor in graph[current]:

            if neighbor in distances:
                continue
            else:
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1
                prev[neighbor] = current

    return prev

def get_route(country, prev):
    c = country
    path = [country]
    
    while c in prev:
        path.append(prev[c])
        c = prev[c]
    path.reverse()
    return path
    
prevlist = bfs(graph, "USA")







#defining get endpoints
@app.get("/ping")
def home():
    return {"pong":"Hello"}


# uvicorn main:app --reload to run
#defining get endpoints
@app.get("/{country}")
def home(country: str):
    if country.upper() not in prevlist:
        return {"400" : "Country not found"}


    route = get_route(country.upper(), prevlist)
    return {
        "destination" : country.upper(),
        "route" : route
    }


# uvicorn main:app --reload to run






