import pyaudio
import wave
import whisper

# Audio I/O
FRAMES_PER_BUFFER = 3200    #frames_per_buffer – Specifies the number of frames per buffer.
FORMAT = pyaudio.paInt16    #format – Sampling size and format. See PortAudio Sample Format.
CHANNELS = 1    #channels – Number of channels
RATE =  16000   #rate – Sampling frame rate

# To use PyAudio, first instantiate PyAudio
p = pyaudio.PyAudio()


stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,   #input – Specifies whether this is an input stream. Defaults to False.
    frames_per_buffer = FRAMES_PER_BUFFER
)


print('START recording')

seconds = 5
frames = []
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print('END recording')

obj = wave.open('output.wav','wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames)) #write all elements in frame into binary string
obj.close()


#NLP Model
print('START analyzing')
model = whisper.load_model("base")
result = model.transcribe("output.wav", fp16=False) #FP16 is not supported on CPU; using FP32 instead
print(result["text"])
