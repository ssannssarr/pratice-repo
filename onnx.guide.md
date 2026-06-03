# 🥜 Piper Voice Training on Kaggle – Complete Guide

Complete guide for training / fine-tuning Piper voices on Kaggle, then exporting to ONNX.

Based on:

- Original Piper training guide
- Our Kaggle debugging
- Single GPU setup
- Version notes
- ONNX export patch
- Kaggle file loss lesson

---

## 0. Best Kaggle Setup

**Recommended accelerator:**

```text
GPU: P100
Reason: single GPU, less Lightning/DDP confusion
```

Avoid for first setup:

```text
T4 x2
Reason: two GPUs can confuse PyTorch Lightning / DDP
```

Use one GPU only:

```bash
CUDA_VISIBLE_DEVICES=0
```

This keeps training clean and avoids multi-GPU chaos.

---

## 1. Known Working Environment

This setup reached training checkpoint + ONNX export:

| Component | Version / Value |
|---|---|
| Kaggle Python | `3.12.13` |
| Torch | `2.2.2+cu121` |
| Torchaudio | `2.2.2+cu121` recommended match |
| GPU | `P100` |
| Repo | `OHF-Voice/piper1-gpl` |
| Single GPU env | `CUDA_VISIBLE_DEVICES=0` |

Suggested ONNX compatibility versions if export complains:

```bash
pip install onnx==1.16.2 onnxruntime==1.18.1 onnxscript==0.1.0
```

Important:

```text
Training worked.
Export needed a small code patch.
The real export bug was f=output_path needing f=str(output_path).
```

After any successful run, save exact versions:

```bash
!python --version
!pip show torch torchaudio onnx onnxruntime onnxscript
!pip freeze > /kaggle/working/requirements_working.txt
```

---

## 2. Install System Requirements

Run first:

```bash
!apt-get update
!apt-get install -y build-essential cmake ninja-build
```

Correct:

```bash
apt-get install -y build-essential cmake ninja-build
```

Wrong:

```bash
apt-get build-essential cmake ninja-build
```

Because `apt-get` needs an operation like `install`.

---

## 3. Clone Piper Repo

Use the correct repo:

```bash
!git clone --depth 1 https://github.com/OHF-Voice/piper1-gpl.git
%cd /kaggle/working/piper1-gpl
```

If clone gets stuck or asks GitHub username, use ZIP method:

```bash
!wget -O /kaggle/working/piper.zip https://github.com/OHF-Voice/piper1-gpl/archive/refs/heads/main.zip
!unzip -q /kaggle/working/piper.zip -d /kaggle/working
!mv /kaggle/working/piper1-gpl-main /kaggle/working/piper1-gpl
%cd /kaggle/working/piper1-gpl
```

---

## 4. Install Python Training Requirements

Inside repo:

```bash
!python3 -m pip install -e '.[train]'
```

If Torch gets changed or breaks, reinstall the known working Torch pair:

```bash
!pip uninstall -y torch torchaudio torchvision
!pip install torch==2.2.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121
```

Check:

```bash
!python --version
!pip show torch torchaudio
```

Expected note:

```text
Python 3.12.13
Torch 2.2.2+cu121
```

---

## 5. Build Monotonic Align

Run:

```bash
!./build_monotonic_align.sh
```

Then dev build:

```bash
!python3 setup.py build_ext --inplace
```

This builds Piper's compiled alignment extension.

---

## 6. Dataset Format

Put dataset here:

```text
/kaggle/working/voices/
```

Example:

```text
/kaggle/working/voices/
├── metadata.csv
├── utt1.wav
├── utt2.wav
├── utt3.wav
```

CSV format:

```csv
utt1.wav|Text for utterance 1.
utt2.wav|Text for utterance 2.
utt3.wav|Text for utterance 3.
```

Check:

```bash
!ls -lah /kaggle/working/voices
!head /kaggle/working/voices/metadata.csv
!find /kaggle/working/voices -name "*.wav" | head
```

---

## 7. Check Audio Duration

```python
import os, wave

total = 0
folder = "/kaggle/working/voices"

for f in os.listdir(folder):
    if f.endswith(".wav"):
        path = os.path.join(folder, f)
        with wave.open(path, "rb") as w:
            total += w.getnframes() / w.getframerate()

print(f"Total duration: {total/60:.2f} minutes")
```

Guide:

| Goal | Duration |
|---|---|
| Pipeline test | 30 sec okay |
| Minimum usable | 10 min |
| Good | 30 min+ |
| Better | 1 hour+ |

Splitting short clips does not create more data. It only creates more pieces.

---

## 8. Training Variables

| Variable | Meaning |
|---|---|
| `voice_name` | name of voice |
| `csv_path` | path to `metadata.csv` |
| `audio_dir` | folder containing audio files |
| `sample_rate` | usually `22050` |
| `espeak_voice` | language voice, example `en-us` |
| `cache_dir` | cache for phonemes/audio artifacts |
| `config_path` | output JSON config path |
| `batch_size` | training batch size |
| `ckpt_path` | optional fine-tune checkpoint |

Our test values:

```text
voice_name   = sann
csv_path     = /kaggle/working/voices/metadata.csv
audio_dir    = /kaggle/working/voices
sample_rate  = 22050
espeak_voice = en-us
cache_dir    = /kaggle/working/cache
config_path  = /kaggle/working/sann.json
batch_size   = 16
GPU env      = CUDA_VISIBLE_DEVICES=0
```

---

## 9. Basic Training Command

```bash
!CUDA_VISIBLE_DEVICES=0 python3 -m piper.train fit \
  --data.voice_name "sann" \
  --data.csv_path /kaggle/working/voices/metadata.csv \
  --data.audio_dir /kaggle/working/voices \
  --model.sample_rate 22050 \
  --data.espeak_voice en-us \
  --data.cache_dir /kaggle/working/cache \
  --data.config_path /kaggle/working/sann.json \
  --data.batch_size 16 \
  --trainer.accelerator gpu \
  --trainer.devices 1
```

Batch size notes:

```text
32 = faster but more VRAM
16 = safer on Kaggle
8  = use if VRAM error
4  = last safe fallback
```

---

## 10. Training With Fine-Tune Checkpoint

Recommended for real training:

```bash
!CUDA_VISIBLE_DEVICES=0 python3 -m piper.train fit \
  --data.voice_name "sann" \
  --data.csv_path /kaggle/working/voices/metadata.csv \
  --data.audio_dir /kaggle/working/voices \
  --model.sample_rate 22050 \
  --data.espeak_voice en-us \
  --data.cache_dir /kaggle/working/cache \
  --data.config_path /kaggle/working/sann.json \
  --data.batch_size 16 \
  --trainer.accelerator gpu \
  --trainer.devices 1 \
  --ckpt_path /kaggle/working/finetune.ckpt
```

Use `--ckpt_path` because:

- speeds up training
- avoids starting from zero
- medium Piper checkpoints are safest for normal fine-tuning

---

## 11. Watch GPU

```bash
!nvidia-smi
```

If GPU is active, Python should be using GPU memory.

---

## 12. Find Checkpoints

Checkpoints are usually saved in:

```text
lightning_logs/version_*/checkpoints/
```

Find them:

```bash
!find /kaggle/working -name "*.ckpt"
```

Example from our test:

```text
/kaggle/working/piper1-gpl/lightning_logs/version_2/checkpoints/epoch=40-step=82.ckpt
```

---

## 13. When to Stop Training

For tiny pipeline test:

```text
30 sec data
6 clips
Epoch 40 proved pipeline worked
```

For real dataset:

- do not judge by epoch only
- watch loss
- use enough clean audio
- save checkpoints often

Pipeline test success means:

- training starts
- GPU works
- checkpoint is created
- no crash

---

## 14. Backup Before Export or Stop Session

Kaggle can delete `/kaggle/working` when session stops.

Backup immediately after checkpoint/export:

```bash
!mkdir -p /kaggle/working/safe
!cp /kaggle/working/*.onnx /kaggle/working/safe/ 2>/dev/null || true
!cp /kaggle/working/*.json /kaggle/working/safe/ 2>/dev/null || true
!cp /kaggle/working/requirements_working.txt /kaggle/working/safe/ 2>/dev/null || true
!cp -r /kaggle/working/piper1-gpl/lightning_logs /kaggle/working/safe/ 2>/dev/null || true
!zip -r /kaggle/working/piper_safe_backup.zip /kaggle/working/safe
```

Then download `piper_safe_backup.zip` from Kaggle right panel.

Important:

```text
Restart kernel = files may stay
Stop session = /kaggle/working files can vanish
Download important outputs immediately
```

---

## 15. Export to ONNX

Original command:

```bash
!python3 -m piper.train.export_onnx \
  --checkpoint /path/to/checkpoint.ckpt \
  --output-file /path/to/model.onnx
```

Example:

```bash
!python3 -m piper.train.export_onnx \
  --checkpoint /kaggle/working/piper1-gpl/lightning_logs/version_2/checkpoints/epoch=40-step=82.ckpt \
  --output-file /kaggle/working/sann.onnx
```

---

## 16. Export Error We Got

Error:

```text
BeartypeCallHintParamViolation
torch.onnx.export() parameter f=PosixPath('/kaggle/working/sann.onnx') violates type hint
```

Meaning:

```text
Piper passed output_path as pathlib.PosixPath.
torch.onnx.export expected str / bytes.
```

This is not a training issue. It is an export script type bug.

---

## 17. Export Fix

File:

```text
/kaggle/working/piper1-gpl/src/piper/train/export_onnx.py
```

Find:

```python
torch.onnx.export(
    model=model_g,
    args=dummy_input,
    f=output_path,
    verbose=False,
    opset_version=OPSET_VERSION,
    input_names=["input", "input_lengths", "scales", "sid"],
    output_names=["output"],
)
```

Change:

```python
f=output_path
```

to:

```python
f=str(output_path)
```

Automatic patch:

```bash
!python3 - <<'PY'
p = "/kaggle/working/piper1-gpl/src/piper/train/export_onnx.py"

s = open(p).read()
s = s.replace("f=output_path", "f=str(output_path)")
open(p, "w").write(s)

print("patched output_path")
PY
```

Verify:

```bash
!sed -n '85,110p' /kaggle/working/piper1-gpl/src/piper/train/export_onnx.py
```

Export again:

```bash
!python3 -m piper.train.export_onnx \
  --checkpoint /kaggle/working/piper1-gpl/lightning_logs/version_2/checkpoints/epoch=40-step=82.ckpt \
  --output-file /kaggle/working/sann.onnx
```

---

## 18. Final Output Files

After successful export:

```text
sann.onnx
sann.json
```

Piper-compatible names:

```text
en_US-sann-medium.onnx
en_US-sann-medium.onnx.json
```

Rename:

```bash
!cp /kaggle/working/sann.onnx /kaggle/working/en_US-sann-medium.onnx
!cp /kaggle/working/sann.json /kaggle/working/en_US-sann-medium.onnx.json
```

Check:

```bash
!ls -lah /kaggle/working/*.onnx /kaggle/working/*.json
```

---

## 19. Zip Final Model

```bash
!zip -j /kaggle/working/sann_piper_voice.zip \
  /kaggle/working/en_US-sann-medium.onnx \
  /kaggle/working/en_US-sann-medium.onnx.json \
  /kaggle/working/requirements_working.txt
```

Download immediately from Kaggle right panel.

---

## 20. Common Errors

### `apt-get build-essential invalid operation`

Wrong:

```bash
!apt-get build-essential cmake ninja-build
```

Correct:

```bash
!apt-get install -y build-essential cmake ninja-build
```

### Git clone asks username

Use:

```text
https://github.com/OHF-Voice/piper1-gpl.git
```

Or use ZIP method.

### Two GPU confusion

Use:

```bash
CUDA_VISIBLE_DEVICES=0
```

and:

```bash
--trainer.devices 1
```

### VRAM error

Lower batch size:

```text
32 → 16 → 8 → 4
```

### `PosixPath not str` during export

Patch:

```python
f=str(output_path)
```

### `onnxscript.values has no attribute ParamSchema`

Likely ONNX / Torch version mismatch.

Try:

```bash
!pip uninstall -y onnxscript onnx onnxruntime
!pip install onnx==1.16.2 onnxruntime==1.18.1 onnxscript==0.1.0
```

But in our successful path, the main blocker was the `PosixPath` export bug.

---

## 21. Big Real Training Checklist

Before doing a long run:

- use P100 or stable single GPU
- set `CUDA_VISIBLE_DEVICES=0`
- set `--trainer.devices 1`
- use clean 22050 Hz audio
- use one speaker
- remove background noise/music
- keep `metadata.csv` clean
- use 10 min minimum, 30 min+ better
- use `--ckpt_path` fine-tune checkpoint
- save `requirements_working.txt`
- zip checkpoint + config + final outputs
- download outputs immediately

---

## 22. Full Big Training Template

```bash
!CUDA_VISIBLE_DEVICES=0 python3 -m piper.train fit \
  --data.voice_name "YOUR_NAME" \
  --data.csv_path /kaggle/working/voices/metadata.csv \
  --data.audio_dir /kaggle/working/voices \
  --model.sample_rate 22050 \
  --data.espeak_voice en-us \
  --data.cache_dir /kaggle/working/cache \
  --data.config_path /kaggle/working/YOUR_NAME.json \
  --data.batch_size 16 \
  --trainer.accelerator gpu \
  --trainer.devices 1 \
  --ckpt_path /kaggle/working/finetune.ckpt
```

---

## 23. Full Export Template

Find checkpoint:

```bash
!find /kaggle/working -name "*.ckpt"
```

Patch export:

```bash
!python3 - <<'PY'
p = "/kaggle/working/piper1-gpl/src/piper/train/export_onnx.py"
s = open(p).read()
s = s.replace("f=output_path", "f=str(output_path)")
open(p, "w").write(s)
print("patched output_path")
PY
```

Export:

```bash
!python3 -m piper.train.export_onnx \
  --checkpoint /kaggle/working/piper1-gpl/lightning_logs/version_X/checkpoints/YOUR_CHECKPOINT.ckpt \
  --output-file /kaggle/working/YOUR_NAME.onnx
```

Rename:

```bash
!cp /kaggle/working/YOUR_NAME.onnx /kaggle/working/en_US-YOUR_NAME-medium.onnx
!cp /kaggle/working/YOUR_NAME.json /kaggle/working/en_US-YOUR_NAME-medium.onnx.json
```

Zip:

```bash
!pip freeze > /kaggle/working/requirements_working.txt
!zip -j /kaggle/working/YOUR_NAME_piper_voice.zip \
  /kaggle/working/en_US-YOUR_NAME-medium.onnx \
  /kaggle/working/en_US-YOUR_NAME-medium.onnx.json \
  /kaggle/working/requirements_working.txt
```

---

## 24. Final Flow

```text
Install system packages
↓
Clone piper1-gpl
↓
Install train dependencies
↓
Build monotonic align
↓
Prepare metadata.csv + wav files
↓
Train with CUDA_VISIBLE_DEVICES=0
↓
Find checkpoint
↓
Backup checkpoint/config
↓
Patch export_onnx.py
↓
Export ONNX
↓
Rename ONNX + JSON
↓
Zip final voice
↓
Download immediately
```

Tiny data proves the pipeline.

Big clean data makes the real voice.
