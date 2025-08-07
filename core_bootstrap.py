core_bootstrap.py

AI albayancor - نقطة البدء المركزية

التمهيد للنواة، تفعيل الجسر، الاتصال بالمستودع

import os import sys import json import threading from pathlib import Path

--- المرحلة 1: تعريف البيئة الأولية ---

PROJECT_ROOT = Path(file).parent.resolve() CONFIG_PATH = PROJECT_ROOT / "config.json"

if not CONFIG_PATH.exists(): default_config = { "node_id": "albayancor-node-001", "bridge_enabled": True, "repository_url": "https://github.com/HarasAlLisan/AI-albayancor", "auto_pull": True, "core_modules": ["bridge/bridge_node.py", "core/ai_engine.py"] } CONFIG_PATH.write_text(json.dumps(default_config, indent=4))

--- المرحلة 2: تحميل الإعدادات ---

with open(CONFIG_PATH) as f: config = json.load(f)

NODE_ID = config.get("node_id") REPO_URL = config.get("repository_url")

print(f"\n🚀 [AI albayancor] تهيئة النواة {NODE_ID}") print(f"🔗 ربط المستودع: {REPO_URL}")

--- المرحلة 3: تحميل الجسر ---

try: from bridge.bridge_node import activate_bridge except ImportError: print("❌ لم يتم العثور على الجسر التقني. تأكد من هيكل المجلد.") sys.exit(1)

--- المرحلة 4: تفعيل الاتصال ---

def start_node(): print("\n🧠 تفعيل الجسر الذكي وبدء الاتصال اللامركزي...") activate_bridge(config)

threading.Thread(target=start_node).start()

--- ملاحظة ---

هذه فقط نقطة التفعيل الأولى، سيتم لاحقًا:

- تحميل النواة الذكية (ai_engine.py)

- تحليل الشبكة المحيطة

- تفعيل نقاط التأثير

نهاية bootstrap

