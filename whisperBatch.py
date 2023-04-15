import os
import time
import shutil
import whisper
os.chdir(os.path.dirname(__file__)) # change the current dir to the file' dir

recorderPath="H:\\REC_FILE\\FOLDER01"
unTransedPath=".\\unTransed_audio"
transedPath=".\\transed_audio"
transResultPath=".\\trans_result"
DEVICE = 'cuda'
MODEL="medium"

try:    # get all .mp3 files under {recorderPath}
    recorderFiles = [file for file in os.listdir(recorderPath) if os.path.splitext(file)[1] == ".mp3"] 
except Exception as e:
    recorderFiles=[]
    print(e)

if recorderFiles==[]:
    print("no file to move")
else:
    for file in recorderFiles:      # move .mp3 files from recorder to local
        print(f"moving {file}")
        shutil.move(recorderPath+"\\"+file,unTransedPath)

# get all un-transcribed files
print("transcription start")
unTransedFiles=[file for file in os.listdir(unTransedPath) if os.path.splitext(file)[1] == ".mp3"]
if unTransedFiles==[]:
    print("no file to transcribe")
else:   # transcribe
    model = whisper.load_model(MODEL, device = DEVICE)
    for file in unTransedFiles:
        transStartTime=time.time()
        print(f"transcribing {file}")
        result = model.transcribe(unTransedPath+"\\"+file)      # this line calls whisper
        transElapsedTime=time.time()-transStartTime
        print(f"elapsed time {transElapsedTime}")
        with open(transResultPath + "\\" + os.path.splitext(file)[0] + ".txt", "w") as f:
            f.write(result["text"])
        shutil.move(unTransedPath+"\\"+file, transedPath)
    print("transcription finished")