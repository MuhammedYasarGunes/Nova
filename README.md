# Nova · Yerel AI Agent

Tamamen yerelde çalışan, araç kullanabilen ve konuşmaları hatırlayan deneysel bir AI agent. Ollama üzerinden yerel bir LLM (Qwen 2.5) kullanır; dışarıya API çağrısı yapmaz.

> **English:** An experimental local AI agent. It routes each request with an LLM (Ollama + Qwen 2.5) to a tool or to plain chat, runs tools such as a terminal command runner (with user confirmation), and keeps a semantic memory in ChromaDB using sentence-transformers embeddings.

## Nasıl çalışır

```text
Kullanıcı girdisi
      ↓
Hafızaya kaydet + benzer eski konuşmaları getir (ChromaDB)
      ↓
Planner: LLM, isteğe uygun aracı JSON olarak seçer
      ↓
Araç seçildiyse çalıştır (terminal komutları kullanıcı onayıyla)
      ↓
LLM, araç çıktısını ve hafızayı kullanarak cevap üretir
```

- **Planner** (`core/planner/`): `TOOL_SCHEMA` içindeki araç listesine göre LLM'den `{"tool": ..., "input": ...}` biçiminde JSON ister; cevap JSON değilse normal sohbete düşer.
- **Araçlar** (`tools/`): her araç `BaseTool`'dan türer ve `tool_registry.py`'ye kaydedilir. Şu an tek araç `terminal`.
- **Hafıza** (`core/memory/`): her mesaj sentence-transformers ile vektöre çevrilir, ChromaDB'ye (`database/`) yazılır; yeni bir mesajda en yakın 3 kayıt bağlama eklenir.
- **LLM** (`core/llm/`): Ollama istemcisi; varsayılan model `qwen2.5:7b`.

## Kurulum

```bash
git clone https://github.com/MuhammedYasarGunes/Nova.git
cd Nova
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Ollama (macOS)
brew install ollama
ollama serve            # ayrı bir terminalde
ollama pull qwen2.5:7b
```

## Çalıştırma

```bash
python3 main.py
```

```text
Sen > hangi klasördeyim
Çalıştırılacak komut: pwd
Onaylıyor musun? [e/H] e
Agent > Şu an /Users/... klasöründesin.

Sen > ben ne çalışıyordum?
Agent > (hafızadaki önceki konuşmalara göre cevap)
```

Çıkmak için `exit` yaz.

## Proje yapısı

```text
core/
  agent/       Agent: hafıza → planner → araç → cevap akışı
  llm/         Ollama istemcisi
  memory/      embedding, ChromaDB vektör deposu, hafıza yöneticisi
  planner/     LLM tabanlı araç seçimi ve araç şeması
tools/
  base_tool.py      araçların ortak arayüzü
  tool_registry.py  kayıtlı araçlar
  terminal/         terminal komutu çalıştıran araç
main.py        sohbet döngüsü
```

## Güvenlik notu

Terminal aracı LLM'in seçtiği komutu kabukta çalıştırır. Bu yüzden her komut çalıştırılmadan önce ekranda gösterilir ve onayın istenir. Varsayılan cevap "hayır"dır. Yine de yalnızca kendi bilgisayarında, güvendiğin bir ortamda kullan.

## Yol haritası

- Çok adımlı planlama (ReAct döngüsü)
- Dosya sistemi ve web otomasyonu araçları
- Sesli asistan (Whisper + TTS)
- Hafızayı zamanla özetleme ve temizleme

## Geliştiren

[Muhammed Yaşar Güneş](https://github.com/MuhammedYasarGunes)
