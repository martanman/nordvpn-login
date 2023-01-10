### Outline

Automates NordVPN login process on Linux for the NordVPN command-line utility. NordVPN requires browser login and copying the auth callback link back to the terminal; this automates that process with [playwright stealth](https://github.com/AtuboDad/playwright_stealth/) because NordVPN uses bot detection.

### Installation

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Usage

Fill in the `./nord-login` file with the project directory, and account email & password. Then run

```
chmod +x ./nord-login
```

to make it executable, and copy the file somewhere to your PATH. You can then run it just with

```
$ nord-login
```

You can also run `login.py` directly with

```
python login.py <email> <password>
```

after sourcing the python virtual environment.
