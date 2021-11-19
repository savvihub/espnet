import argparse
import time
import os
import uuid

import streamlit as st
import soundfile as sf

from espnet2.bin.tts_inference import Text2Speech


def elapsed_time(fn, *args):
    start = time.time()
    output = fn(*args)
    end = time.time()

    elapsed = f'{end - start:.2f}'

    return elapsed, output


def inference(models):
    input_str = st.text_input(
        label="Write your favorite sentence in English",
    )

    if input_str:
        for model in models:
            st.success(f'Create \"{input_str}\" with {model.name}...')
            elapsed, input_wav = elapsed_time(model.tts, input_str)
            st.write(f'- Inference time: {elapsed} seconds')

            filename = str(uuid.uuid4())[:8] + ".wav"
            filepath = os.path.join(model.path, filename)
            if not os.path.exists(filepath):
                st.write(f'Sentence: {input_str}')
                sf.write(filepath, input_wav["wav"].view(-1).cpu().numpy(), model.tts.fs, 'PCM_24')

            if os.path.exists(filepath):
                st.audio(filepath)


def read_file(path):
    return open(path).read()


class TTSModel:
    def __init__(self, tts, name):
        self.name = name
        self.path = name + "_wav"
        self.tts = tts

def main(args):
    models = [
        TTSModel(Text2Speech.from_pretrained(
            train_config="exp/tts_train_raw_phn_tacotron_g2p_en_no_space/config.yaml",
            model_file="exp/tts_train_raw_phn_tacotron_g2p_en_no_space/40epoch.pth",
        ), "tacotron2"),
        TTSModel(Text2Speech.from_pretrained(
            train_config="exp/tts_train_raw_phn_tacotron_g2p_en_no_space/config.yaml",
            model_file="exp/tts_train_raw_phn_tacotron_g2p_en_no_space/40epoch.pth",
            vocoder_tag="parallel_wavegan/ljspeech_style_melgan.v1",
        ), "tacotron2_vocoder"),
    ]

    for model in models:
        if not os.path.exists(model.path):
            os.makedirs(model.path)

    st.title("[Vessl AI] Tacotron2 Demo")

    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        ["Instruction", "Inference", "Source code"]
    )

    if app_mode == "Instruction":
        st.write('## To inference with the pretrained model:\n'
                 '1. Click **Inference** app mode on the side bar\n'
                 '2. Write your favorite sentence in English\n'
                 '3. Press Enter\n'
                 '4. The inference result will show up\n'
                 '## To show the source code:\n'
                 '1. Click **Source code** app mode on the side bar\n'
                 '2. The source code will show up')
    elif app_mode == "Inference":
        inference(models)
    elif app_mode == "Source code":
        st.code(read_file(args.app_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Streamlit Tacotron2 Demo')
    parser.add_argument('--app-path', type=str, default='egs2/ljspeech/tts1/app.py', help='app path')
    args = parser.parse_args()
    main(args)
