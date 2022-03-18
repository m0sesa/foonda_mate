## CLI APP | Monitor userbase growth

This is a demo cli application that helps to monitor userbase growth across a period of time. Please note that you need to be connected to the internet to use this tool.

## Installation
### Set up
```bash
cd foonda_mate
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
```

### Run tests
If you are already in the directory you can skip the first line
```bash
cd foonda_mate
python -m unittest discover ./tests
```

### App use
If you are already in the directory you can skip the first line

#### Get Help
```bash
cd foonda_mate
python3 ./src/main.py [COMMAND]

```

#### Available commands
- get_filtered

e.g
```bash
python3 ./src/main.py get_filtered 1-1-2022 12-1-2022
```