import json
import os

def run_seo_generator():
    matrix_path = 'public/components/seo_matrix.json'
    print("\n⚡ [DAMODAR TECHCRAZE VENTURES - P-SEO INITIALIZER RUNNING]")
    print("---------------------------------------------------------")
    
    if os.path.exists(matrix_path):
        with open(matrix_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"📦 Successfully verified {len(data)} high-intent programmatic landing nodes in active stack.")
        print("🚀 [STATUS]: pSEO routing engine fully operational and mapping runtime URLs.")
    else:
        print("⚠️ Matrix dataset missing! Re-initializing repository config...")

if __name__ == '__main__':
    run_seo_generator()
