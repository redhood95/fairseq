import torch
import fairseq
import torchaudio


from utils import split_audio , load_splitted_audio

model_path = r'D:\interviews\fairseq\weights\wav2vec_large.pt'
f_name = r'D:\interviews\fairseq\audio_file\yash.flac'
output_path = r'D:\interviews\fairseq\audio_file\splits'
split_audio(f_name,split_length=78960*3,output_path=output_path)
audio_tensors = load_splitted_audio(output_path)

model, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([model_path])
model = model[0]
model.eval()

print("running feature extractor")

for i,at in enumerate(audio_tensors):
    z = model.feature_extractor(at)
    c = model.feature_aggregator(z)
    print(c)


