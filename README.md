# Hermes Core — Yerel AI Agent Sistemi
Hermes Core, tamamen yerel çalışan, tool kullanabilen ve hafıza tutabilen AI agent altyapısıdır.
Bu proje:
- Ollama üzerinden yerel LLM çalıştırır
- Terminal ve sistem araçlarını kullanabilir
- Semantic memory (vektör hafıza) içerir
- LLM tabanlı tool routing yapar
- Genişletilebilir agent mimarisi sunar
---
# 🚀 Özellikler
## 🧠 Yerel Yapay Zeka
- Ollama üzerinden Qwen modeli çalıştırılır
- API bağımlılığı yoktur
- Tamamen offline kullanılabilir
## 🔧 Tool Sistemi
- Terminal komutları çalıştırma
- Genişletilebilir tool mimarisi
- LLM tabanlı tool seçimi (JSON format)
## 🧠 Hafıza Sistemi
- ChromaDB tabanlı vektör hafıza
- Semantic search desteği
- Kullanıcı geçmişini hatırlama
## 💬 Chat Agent
- Sürekli sohbet döngüsü
- Bağlam (context) desteği
- Hafızadan bilgi çekme
---
# 🏗 Sistem Mimarisi
```text id="r2"
Kullanıcı Girdisi
      ↓
Planner (LLM Router)
      ↓
Tool Seçimi (JSON)
      ↓
Tool Çalıştırma
      ↓
Hafıza Sorgulama
      ↓
LLM Yanıt Üretimi

⸻

📦 Kurulum

1. Repoyu klonla

git clone <repo-url>
cd hermes-core

⸻

2. Sanal ortam oluştur

uv venv
source .venv/bin/activate

⸻

3. Gerekli paketler

uv pip install ollama chromadb sentence-transformers rich pydantic

⸻

4. Ollama kurulumu

brew install ollama
ollama serve
ollama pull qwen2.5:7b

⸻

▶️ Çalıştırma

python3 main.py

⸻

💬 Kullanım

Örnek 1 — Terminal Tool

Sen > hangi klasördeyim
Agent > /Users/...

Örnek 2 — Hafıza sorgusu

Sen > ben ne çalışıyordum?
Agent > ...

⸻

📁 Proje Yapısı

hermes-core/
│
├── core/
│   ├── agent/
│   ├── llm/
│   ├── planner/
│   └── memory/
│
├── tools/
│   ├── terminal/
│   ├── router.py
│
├── database/
├── main.py
└── README.md

⸻

⚠️ Notlar

* Bu proje deneysel bir AI agent sistemidir
* Üretim (production) için optimize değildir
* Hafıza sistemi zamanla büyür (ileride temizleme gerekir)
* LLM promptları modele göre ayarlanabilir

⸻

🔮 Gelecek Geliştirmeler

* Çok adımlı planlama (ReAct loop)
* Dosya sistemi araçları
* Web otomasyonu (Playwright)
* Sesli asistan (Whisper + TTS)
* Multi-agent mimarisi
* Görev zamanlama sistemi

⸻

🧠 Felsefe

Bu proje şu prensibe dayanır:

“LLM tek başına karar vermez, araç kullanır ve kontrollü bir sistem içinde çalışır.”

⸻

📌 Amaç

Bu sistemin amacı:

* yerel çalışan AI agent altyapısı kurmak
* araç kullanan gerçek bir “dijital asistan” geliştirmek
* zamanla otonom sistemlere evrilmek

⸻
