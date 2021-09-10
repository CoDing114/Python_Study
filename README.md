# Python_Study

Ctrl + P 를 눌러  launch.json  파일을 찾는다

Python 구성에  "cwd": "${fileDirname}"  을 추가해준다 


{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File (Integrated Terminal)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${fileDirname}" //  "Current File" 
        },
    ]
}
