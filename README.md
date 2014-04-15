# Python Code Signing

## Goal

Solve this puzzle by extracting your secret token from the file "secret".
You can start the puzzle locally by executing:

```
./run
```

## Overview

Python implementation of code signing for secure remote code execution. Works with both Python 2.x and 3.x.

```bash
pip install -r requirements.txt
```

Features:
 * ECDSA with curve brainpoolP256r1.
 * SHA-3 hash
 * Fast RNG

Start the server on port 4533 using the private key in the file "key.hex" with signing enabled:
```bash
python lib/server.py --port=4533 --key-file=key.hex --signing=true
```

Sign and run the code in the file "test.py" and display results to standard out:
```bash
cat test.py | curl -XPOST http://localhost:4533/sign --data-binary @- | curl -XPOST http://localhost:4533/execute --data-binary @-
```

Sign code in the file "test.py" and save to "test.pys":
```bash
cat test.py | curl -XPOST http://localhost:4533/sign --data-binary @- > test.pys
```

Run previously signed code in "test.pys" and display results to standard out:
```bash
cat test.pys | curl -XPOST http://localhost:4533/execute --data-binary @-
```

Fetch an existing peice of stored code:
```bash
curl -XGET http://localhost:4533/code/hello.py > hello.pys
```

