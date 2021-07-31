import soundfile as sf 
import os
import torchaudio 


def split_audio(path_to_audio,split_length,output_path):
    wave, sample_rate = sf.read(path_to_audio)
    wave1 = wave[:,0] 
    wave1 = wave1.reshape(len(wave1))
    counter = 0
    for i in range(0,len(wave1),split_length):
        if (i+split_length) < len(len(wave1)):
            wave_split = wave1[i:i+split_length]
        else:
            wave_split = wave1[i:]
        counter += 1
        sf.write(os.path.join(output_path,str(counter)+'.flac'), wave_split,int( sample_rate))

    return wave,sample_rate


def load_splitted_audio(path):
    return 0

