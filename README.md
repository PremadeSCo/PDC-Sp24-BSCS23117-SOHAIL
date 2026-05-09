# PDC-Sp24-BSCS23117-SOHAIL

## How to run

### Prereq

```bash
python3 -m venv myenv # or whatever python you have
source myenv/bin/activate
pip install -r requirements.txt
```

### Linux
```bash
sh run.sh
```

### Windows 
> Prefer linux because it's not tested on windows
```bash
uvicorn src.app:app --workers 4 
```

Server should start at port $8000$ `127.0.0.1:8000`

## Test
To test the concurrency fix
```bash
python3 test_fix.py
```

This should send two requests concurrently to the /api/generate-challenge endpoint. 
Since these are almost sent at the same time one of them should result in 409 conflict. Previosuly both would be 200 but the later request would have silently overwritten the response 
I'm using versioning technique

## Notes
I modified the `generate_challenge_with_ai` to sleep for 2 seconds and just return a dummy response, since i don't have an openai API key. This si required for testing with my script

`OPENAI_API_KEY` is set to a dummy string to prevent crash
