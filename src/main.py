from fastapi import FastAPI
from search import query_quran

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Bayyan AI API"}

@app.get("/search")
def search(q: str):
    results = query_quran(q)

    # Let's format the response nicely for your Node.js bot
    formatted_results = []
    for i in range(len(results['documents'][0])):
        formatted_results.append({
            "text": results['documents'][0][i],
            "surah": results['metadatas'][0][i]['surah_name'],
            "ayah": results['metadatas'][0][i]['ayah_no'],
            "arabic": results['metadatas'][0][i]['arabic_text']
        })
    
    return {"query": q, "matches": formatted_results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
