# HT6-2024


## Setup

set up your env file with .env.example


For Adobe Express:

```zsh
cd qr_code
npm install
npm run build
npm run start
```
---

For Clippy:
    
```zsh

python main.py
``` 


For Clippy to communicate with Adobe Express, Flask:

```zsh
python sse_server.py
```


## Tgt

```zsh
python sse_server.py
cd qr_code
npm run start
python main.py
```

---