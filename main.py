from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from summarize import summarize  


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if file.content_type != 'text/plain':
        raise HTTPException(status_code=400, detail='Only text files are allowed.')

    print('Here')

    text = file.file.read().decode('utf-8')
    summarized_text = summarize(text)
    print(summarized_text)

    return {"filename": file.filename, "summarized_text": summarized_text}