import uvicorn

if __name__ == "__main__":
    uvicorn.run('Main:app', host="0.0.0.0", port=7000, reload=True)