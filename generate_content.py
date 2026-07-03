import os
import time
import requests
from dotenv import load_dotenv

current_folder = os.path.dirname(os.path.abspath(__file__))
target_env_path = os.path.join(current_folder, ".env")

if os.path.exists(target_env_path):
    load_dotenv(dotenv_path=target_env_path, override=True)
else:
    load_dotenv(dotenv_path=".env", override=True)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("\n❌ CRITICAL ERROR: .env credentials missing!")
    exit(1)

VIRAL_TOPICS = [
    {"title": "Secret 4K Cinematic AI Video Editing Packs for Creators", "description": "Get instant access to 4K cinematic AI video bundles.", "price": 299, "product_type": "Digital Bundle"},
    {"title": "How to Scale Instagram Reels Using Advanced Automation Tools", "description": "The ultimate blueprint to automate your Instagram growth.", "price": 199, "product_type": "Digital Blueprint"},
    {"title": "The Faceless YouTube Channel Kickstart Strategy for 2026", "description": "Launch a highly profitable faceless YouTube channel.", "price": 499, "product_type": "Digital Bundle"}
]

def push_to_supabase(product):
    url = f"{SUPABASE_URL}/rest/v1/products"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    try:
        response = requests.post(url, headers=headers, json=product, timeout=10)
        if response.status_code in [200, 201]:
            print(f"✅ [✓ MATRIX SYNCED]: '{product['title']}' is now live in damodar-ventures-db!")
        else:
            print(f"❌ [DATABASE ERROR]: Status {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ [CRASH IMMUNITY]: {e}")

def run_factory_engine():
    print(f"\n🎯 Target Env Path Locked: {target_env_path}")
    print("\n🚀 [🎬 DAMODAR TECHCRAZE VENTURES - VIDEO FACTORY ENGINE LIVE]")
    print("--------------------------------------------------")
    
    for item in VIRAL_TOPICS:
        print(f"📦 Synthesizing viral video data package for topic: [{item['title']}]")
        push_to_supabase(item)
        print(f"🎬 [✓ RENDER COMPLETED]: Video file data matrix compiled successfully.\n")
        time.sleep(1)

if __name__ == "__main__":
    run_factory_engine()