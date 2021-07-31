import soundfile as sf 
import os
import torchaudio as ta
import glob 


def split_audio(path_to_audio,split_length,output_path):

    os.makedirs(output_path,exist_ok=True)
    wave, sample_rate = sf.read(path_to_audio)
    wave1 = wave[:,0] 
    wave1 = wave1.reshape(len(wave1))
    counter = 0
    for i in range(0,len(wave1),split_length):
        if (i+split_length) < len(wave1):
            wave_split = wave1[i:i+split_length]
        else:
            wave_split = wave1[i:]
        counter += 1
        sf.write(os.path.join(output_path,str(counter)+'.flac'), wave_split,int( sample_rate))

    return wave,sample_rate


def load_splitted_audio(path):
    audios = glob.glob(f"{path}/*.flac")
    list_of_audio_tensors = []
    for a in audios:
        waveform, sample_rate = ta.backend.soundfile_backend.load(a)
        list_of_audio_tensors.append(waveform)
    return list_of_audio_tensors

