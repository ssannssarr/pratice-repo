
# 🥜 Piper Voice Training on Kaggle – Complete Guide

Complete guide for training / fine-tuning Piper voice models on Kaggle.

Based on: Original Piper training guide · Kaggle fixes · ONNX export bug fix · Single GPU setup · Version notes

---

## 0. Best Kaggle Setup

**Recommended Kaggle accelerator:**

```

GPU: P100
Reason: single GPU, less confusion

```

> ⚠️ **Avoid for first setup:** `T4 x2` — Reason: two GPUs can confuse Lightning / DDP

Use this environment variable before training:

```bash
CUDA_VISIBLE_DEVICES=0
```

This forces training to use only one GPU.

---

1. Working Environment Notes

The test worked with:

Component Value
Python 3.12.13
Torch 2.2.2+cu121
GPU P100 (recommended)
Repo OHF-Voice/piper1-gpl

⚠️ Important: Training worked. Export had one bug. Bug was fixed by editing export_onnx.py.

---

2. Install System Requirements

Run in Kaggle:

```bash
!apt-get update
!apt-get install -y build-essential cmake ninja-build
```

⚠️ Important: Use apt-get install -y build-essential cmake ninja-build

Not: apt-get build-essential cmake ninja-build

Because apt-get needs an operation like install.

---

3. Clone Piper Repo

Use the correct repo name:

```bash
!git clone --depth 1 https://github.com/OHF-Voice/piper1-gpl.git
```

Then enter repo:

```bash
%cd /kaggle/working/piper1-gpl
```

💡 If clone gets stuck or asks GitHub username, use ZIP method:

```bash
!wget -O piper.zip https://github.com/OHF-Voice/piper1-gpl/archive/refs/heads/main.zip
!unzip -q piper.zip
!mv piper1-gpl-main piper1-gpl
%cd /kaggle/working/piper1-gpl
```

---

4. Install Python Training Requirements

Inside repo:

```bash
!python3 -m pip install -e '.[train]'
```

If packages conflict, still continue unless training fails.

Check Python and Torch:

```bash
!python --version
!pip show torch
```

Expected from our run:

```
Python 3.12.13
Torch 2.10.0+cu128
```

---

5. Build Monotonic Align

Run:

```bash
!./build_monotonic_align.sh
```

Then dev build:

```bash
!python3 setup.py build_ext --inplace
```

This is needed because training uses Piper's compiled alignment code.

---

6. Dataset Format

Put dataset here:

```
/kaggle/working/voices/
```

Example structure:

```
/kaggle/working/voices/
├── metadata.csv
├── utt1.wav
├── utt2.wav
├── utt3.wav
```

CSV format:

```
utt1.wav|Text for utterance 1.
utt2.wav|Text for utterance 2.
utt3.wav|Text for utterance 3.
```

Check files:

```bash
!ls -lah /kaggle/working/voices
!head /kaggle/working/voices/metadata.csv
```

Check audio files:

```bash
!find /kaggle/working/voices -name "*.wav" | head
```

---

7. Check Audio Duration

Optional but useful:

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

For real training:

Goal Duration
Tiny pipeline test 30 sec okay
Minimum usable 10 min
Good 30 min+
Best 1 hour+

---

8. Training Variables

Main variables:

Variable Description
voice_name name of your voice
csv_path metadata.csv path
audio_dir folder containing wav files
sample_rate audio sample rate, usually 22050
espeak_voice language voice, example en-us
cache_dir cache folder
config_path output JSON config path
batch_size training batch size
ckpt_path optional checkpoint for fine-tuning

Our test values:

```
voice_name = sann
csv_path = /kaggle/working/voices/metadata.csv
audio_dir = /kaggle/working/voices
sample_rate = 22050
espeak_voice = en-us
cache_dir = /kaggle/working/cache
config_path = /kaggle/working/sann.json
batch_size = 16
GPU = CUDA_VISIBLE_DEVICES=0
```

---

9. Training Command

Basic training command:

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

💡 Why batch size 16? Safer on Kaggle. Less VRAM error.

If VRAM error: Use batch_size 8

---

10. Training With Fine-Tune Checkpoint

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

💡 Use --ckpt_path because: It speeds up training a lot. It is better than training from zero. Medium quality Piper checkpoints are safest.

---

11. Watch GPU

```bash
!nvidia-smi
```

If GPU is working, you should see Python using GPU memory.

---

12. Find Checkpoints

After training starts, checkpoints are usually saved inside:

```
lightning_logs/version_*/checkpoints/
```

Find them:

```bash
!find /kaggle/working -name "*.ckpt"
```

Example from our test:

```
/kaggle/working/piper1-gpl/lightning_logs/version_2/checkpoints/epoch=40-step=82.ckpt
```

---

13. When to Stop Training

For test dataset:

· 30 sec data
· 6 clips
· Epoch 40 was enough to prove pipeline works

For real dataset:

· Do not judge by epoch only
· Watch loss
· Use enough clean audio
· Save checkpoints

Pipeline test success means:

· Training starts
· GPU works
· Checkpoint is created
· No crash

---

14. Export to ONNX

Original export command:

```bash
!python3 -m piper.train.export_onnx \
    --checkpoint /path/to/checkpoint.ckpt \
    --output-file /path/to/model.onnx
```

Our actual export command:

```bash
!python3 -m piper.train.export_onnx \
    --checkpoint /kaggle/working/piper1-gpl/lightning_logs/version_2/checkpoints/epoch=40-step=82.ckpt \
    --output-file /kaggle/working/sann.onnx
```

---

15. Export Error We Got

Error:

```
BeartypeCallHintParamViolation
torch.onnx.export() parameter f=PosixPath('/kaggle/working/sann.onnx') violates type hint
```

Meaning:

· Piper passed output_path as pathlib.PosixPath
· torch.onnx.export expected str / bytes

This was not a training problem. It was an export script bug.

---

16. Export Fix

Open this file:

```
/kaggle/working/piper1-gpl/src/piper/train/export_onnx.py
```

Find this part:

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

Automatic patch command:

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

Then export again:

```bash
!python3 -m piper.train.export_onnx \
    --checkpoint /kaggle/working/piper1-gpl/lightning_logs/version_2/checkpoints/epoch=40-step=82.ckpt \
    --output-file /kaggle/working/sann.onnx
```

---

17. Final Output Files

After successful export, you need:

```
sann.onnx
sann.json
```

For Piper-compatible naming:

```
en_US-sann-medium.onnx
en_US-sann-medium.onnx.json
```

Rename:

```bash
!cp /kaggle/working/sann.onnx /kaggle/working/en_US-sann-medium.onnx
!cp /kaggle/working/sann.json /kaggle/working/en_US-sann-medium.onnx.json
```

Final files:

```bash
!ls -lah /kaggle/working/*.onnx /kaggle/working/*.json
```

---

18. Zip Final Model

```bash
!zip -j /kaggle/working/sann_piper_voice.zip \
    /kaggle/working/en_US-sann-medium.onnx \
    /kaggle/working/en_US-sann-medium.onnx.json
```

---

19. Download from Kaggle

Use Kaggle file browser:

· Right sidebar
· Output / Working files
· Download sann_piper_voice.zip

Or save it as dataset output if notebook is committed.

---

20. Common Errors

Error: apt-get build-essential invalid operation

Wrong:

```bash
!apt-get build-essential cmake ninja-build
```

Correct:

```bash
!apt-get install -y build-essential cmake ninja-build
```

Error: Git clone asks username

Use correct repo:

```
https://github.com/OHF-Voice/piper1-gpl.git
```

Not typo names. Or use ZIP download.

Error: Two GPUs confusion

Use:

```bash
CUDA_VISIBLE_DEVICES=0
```

and:

```bash
--trainer.devices 1
```

Error: Batch size / VRAM

Lower batch size:

```
32 → 16 → 8 → 4
```

Error: PosixPath not str during export

Patch:

```python
f=str(output_path)
```

Error: onnxscript.values has no attribute ParamSchema

This is ONNX / Torch version mismatch. Try:

```bash
!pip uninstall -y onnxscript onnx onnxruntime
!pip install onnx==1.16.2 onnxruntime==1.18.1 onnxscript==0.1.0
```

But in our successful path, the real blocker was the PosixPath export bug.

---

21. Big Real Training Checklist

Before doing a big run:

· ✅ Use P100 or stable single GPU
· ✅ Use CUDA_VISIBLE_DEVICES=0
· ✅ Use --trainer.devices 1
· ✅ Use clean 22050 Hz audio
· ✅ Use 10 min minimum, 30 min+ better
· ✅ Use same speaker
· ✅ Remove background noise
· ✅ Keep metadata.csv clean
· ✅ Use fine-tune checkpoint
· ✅ Save output files often
· ✅ Zip checkpoint + config

---

22. Full Big Training Template

🔰 BEGINNER NOTE: The name my_voice below is just an example. Replace it with your own voice name (like alice, john, robot-voice, etc). Keep the same name everywhere — don't mix different names!

Copy this and replace my_voice with your chosen name:

```bash
!CUDA_VISIBLE_DEVICES=0 python3 -m piper.train fit \
    --data.voice_name "my_voice" \
    --data.csv_path /kaggle/working/voices/metadata.csv \
    --data.audio_dir /kaggle/working/voices \
    --model.sample_rate 22050 \
    --data.espeak_voice en-us \
    --data.cache_dir /kaggle/working/cache \
    --data.config_path /kaggle/working/my_voice.json \
    --data.batch_size 16 \
    --trainer.accelerator gpu \
    --trainer.devices 1 \
    --ckpt_path /kaggle/working/finetune.ckpt
```

---

23. Full Export Template

🔰 REMEMBER: Replace my_voice with the same name you used in Section 22 above.

```bash
!python3 -m piper.train.export_onnx \
    --checkpoint /kaggle/working/piper1-gpl/lightning_logs/version_X/checkpoints/YOUR_CHECKPOINT.ckpt \
    --output-file /kaggle/working/my_voice.onnx
```

Then rename:

```bash
!cp /kaggle/working/my_voice.onnx /kaggle/working/en_US-my_voice-medium.onnx
!cp /kaggle/working/my_voice.json /kaggle/working/en_US-my_voice-medium.onnx.json
```

Zip:

```bash
!zip -j /kaggle/working/my_voice_piper_voice.zip \
    /kaggle/working/en_US-my_voice-medium.onnx \
    /kaggle/working/en_US-my_voice-medium.onnx.json
```

---

24. Final Summary

The full working flow:

```
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
Patch export_onnx.py
    ↓
Export ONNX
    ↓
Rename ONNX + JSON
    ↓
Zip final voice ✓
```

🥜 This proves Kaggle can fine-tune and export Piper voices.

Tiny data proves pipeline. Big clean data makes the real voice.

```

