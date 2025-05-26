from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def data1():
    return{"message":"hello"}

@app.get("/api")
def api():
    return[
        {"message":"hello my class"},
        {"message":"hello world"}
    ]

@app.get("/ca")
def hr():
    return[
        {"name":"Tayyab",
         "age":19,
         "class":"AI"
         },
         {"name":"Ali",
         "age":23,
         "class":"AI"
         }
    ]
