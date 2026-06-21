from fastapi import FastAPI, UploadFile , File
from model import predict as model_predict
import uvicorn


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "This is the main api endpoint for the model deployment."}



@app.post("/predict/")
async def predict(input_image: UploadFile = File(...)):
    aloowed_extensions = ["jpg", "jpeg", "png"]
    
    if input_image.filename.split(".")[-1] not in aloowed_extensions:
        return {"message": "Invalid file type. Only jpg, jpeg, and png are allowed."}
    
    image_bytes = await input_image.read()
    
    prediction = model_predict(image_bytes)
    
    return {"prediction": prediction}


if __name__ == "__main__":
    uvicorn.run("app2:app", host="127.0.0.1", port=8000 , reload=True)


