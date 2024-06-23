from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from subprocess import check_output, STDOUT, CalledProcessError, run


def compile_python(code):
    print('Will compile code...')
    sample_file = open("sample.py", "w")
    sample_file.write(code)
    sample_file.close()
    cmd = "python -m py_compile sample.py"
    cmd_arr = ['python', 'sample.py']
    result = {'error': False, 'output': ''}
    try:
        check_output(cmd, stderr=STDOUT, shell=True).decode()
        result['output'] = run(cmd_arr, capture_output=True, text=True).stdout
    except CalledProcessError as e:
        print('Caught compilation error')
        result['output'] = e.output.decode()  # print out the stdout messages up to the exception
        result['error'] = True
    return result


class CodeItem(BaseModel):
    code: str
    lang: str


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health-status")
def get_health():
    return {"status": "healthy"}

@app.post("/compile-code/")
async def compile_code(code_item: CodeItem):
    return compile_python(code_item.code)