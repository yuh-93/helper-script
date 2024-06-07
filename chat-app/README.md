# How to use

## 起動コマンド
```bash
docker build --no-cache -t chatgpt-app .
docker run -e OPENAI_API_KEY={{api_key}} -it chatgpt-app
```