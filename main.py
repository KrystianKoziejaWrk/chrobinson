from fastapi import FastAPI


#web server
app = FastAPI()

#defining get endpoints
@app.get("/ping")
def home():
    return {"pong":"Hello"}


# uvicorn main:app --reload to run
