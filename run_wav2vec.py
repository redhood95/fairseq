import torch
import fairseq
import torchaudio


from utils import split_audio

model_path = r'D:\interviews\fairseq\weights\wav2vec_large.pt'
f_name = r'D:\interviews\fairseq\audio_file\splits\1.flac'

split_audio(f_name,split_length=78960*3,output_path=r'D:\interviews\fairseq\audio_file\splits')

model, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([model_path])
model = model[0]
model.eval()

waveform, sample_rate = torchaudio.backend.soundfile_backend.load(f_name)


print("running feature extractor")
z = model.feature_extractor(waveform)
c = model.feature_aggregator(z)
print(c)

