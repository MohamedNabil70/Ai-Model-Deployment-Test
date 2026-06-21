from fastapi import FastAPI, UploadFile , File
from pydantic import BaseModel
import uvicorn

class myModelInput(BaseModel):
    image: UploadFile = File(...)


app = FastAPI()

@app.post("/predict/")
async def home(input: UploadFile = File(...)):
    aloowed_extensions = ["jpg", "jpeg", "png"]
    
    if input.filename.split(".")[-1] not in aloowed_extensions:
        return {"message": "Invalid file type. Only jpg, jpeg, and png are allowed."}
    
    input_image = await input.read()
    
    with open(f"{uuid.uuid4()}.jpg", "wb") as f:
        f.write(input_image)
        
    return {"message": "File uploaded successfully."}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)