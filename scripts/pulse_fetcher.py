import argparse
import requests
import yaml
import sys
import os

API_ENDPOINT = "https://inbrief.info/api/feed/"

def load_config():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, 'config.yaml')
    if not os.path.exists(config_path):
        config_path = os.path.join(base_dir, 'config.default.yaml')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}

def main():
    parser = argparse.ArgumentParser(description="PulseAI API Fetcher")
    parser.add_argument("--include-categories", type=str)
    parser.add_argument("--exclude-categories", type=str)
    parser.add_argument("--include-sources", type=str)
    parser.add_argument("--exclude-sources", type=str)
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    
    config = load_config()
    params = {}
    
    def apply_param(k, arg_val, cfg_val=None):
        if arg_val:
            params[k] = arg_val
        elif cfg_val:
            params[k] = cfg_val
            
    apply_param("include_categories", args.include_categories, config.get("include_categories"))
    apply_param("exclude_categories", args.exclude_categories, config.get("exclude_categories"))
    apply_param("include_sources", args.include_sources, config.get("include_sources"))
    apply_param("exclude_sources", args.exclude_sources, config.get("exclude_sources"))
    apply_param("hours", args.hours)
    apply_param("limit", args.limit)

    custom_host = config.get("api_host", API_ENDPOINT)
    if custom_host.endswith('/'):
        custom_host = custom_host.rstrip('/')

    try:
        response = requests.get(custom_host, params=params)
        if response.status_code == 429:
            try:
                error_data = response.json()
                detail = error_data.get('detail', "IP Rate Limit Exceeded (Interval or Daily Quota).")
            except Exception:
                detail = "IP Rate Limit Exceeded."
            print(f"Error fetching data: HTTP 429 Too Many Requests -> {detail}")
            sys.exit(1)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        print(f"--- PulseAI: Fetched {len(articles)} items ---")
        for idx, a in enumerate(articles, 1):
            print(f"{idx}. [{a['category'].upper()}] {a['title']} (from {a['source']})")
            print(f"   Summary: {a['summary']}")
            print(f"   Link: {a['url']}")
            print("-" * 40)
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
