from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from main import process_parameters

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_form():
    html_content = (
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Parameter Form</title>
        </head>
        <body>
            <h1>Parameter Form</h1>
            <form action="/submit" method="post">
                <label for="param1">Parameter 1:</label>
                <input type="text" id="param1" name="param1" value="default1">
                <br><br>

                <label for="param2">Parameter 2:</label>
                <input type="text" id="param2" name="param2" value="default2">
                <br><br>

                <label for="param3">Parameter 3:</label>
                <input type="text" id="param3" name="param3" value="default3">
                <br><br>

                <button type="submit">Submit</button>
            </form>
            <div id="result">
                <!-- Result will be displayed here -->
            </div>
        </body>
        </html>
        """
    )
    return HTMLResponse(content=html_content)


@app.post("/submit", response_class=HTMLResponse)
def submit_form(
    param1: str = Form(...), param2: str = Form(...), param3: str = Form(...)
):
    result = process_parameters(param1, param2, param3)
    html_content = (
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Result</title>
        </head>
        <body>
            <h1>Parameter Form</h1>
            <form action="/submit" method="post">
                <label for="param1">Parameter 1:</label>
                <input type="text" id="param1" name="param1" value="{param1}">
                <br><br>

                <label for="param2">Parameter 2:</label>
                <input type="text" id="param2" name="param2" value="{param2}">
                <br><br>

                <label for="param3">Parameter 3:</label>
                <input type="text" id="param3" name="param3" value="{param3}">
                <br><br>

                <button type="submit">Submit</button>
            </form>
            <div id="result">
                <h2>Result:</h2>
                <p>{result}</p>
            </div>
        </body>
        </html>
        """
    )
    return HTMLResponse(content=html_content)
