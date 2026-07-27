In your environment, setup 

```bash
export SORUXGPT_GPT_AUTH_TOKEN=<the key you get from platform>
```

then, open `~/.codex/config.toml` and edit

```toml
model_provider = "soruxgpt"
model_reasoning_effort = "max"

[model_providers.soruxgpt]
name = "SoruxGPT API"
base_url = "https://ai.soruxgpt.com/v1"
wire_api = "responses"
env_key = "SORUXGPT_GPT_AUTH_TOKEN"

[features] 
remote_connections = true
goals = true
js_repl = false
```