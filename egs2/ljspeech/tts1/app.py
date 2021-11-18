import argparse
import time
import torch

import streamlit as st
import soundfile as sf

from espnet2.bin.tts_inference import Text2Speech


def elapsed_time(fn, *args):
    start = time.time()
    output = fn(*args)
    end = time.time()

    elapsed = f'{end - start:.2f}'

    return elapsed, output


def inference(text2speech):
    x = st.text_input(
        label="Write your favorite sentence in English",
    )

    elapsed, wav = elapsed_time(text2speech, x)
    st.write(f'- Inference: {elapsed} seconds')

    sf.write('test.wav', wav["wav"].view(-1).cpu().numpy(), text2speech.fs, 'PCM_24')

    st.write("Audio:")
    st.audio('test.wav')


def read_file(path):
    return open(path).read()


def main(args):
    text2speech = Text2Speech.from_pretrained(
        train_config="exp/tts_train_raw_phn_tacotron_g2p_en_no_space/config.yaml",
        model_file="exp/tts_train_raw_phn_tacotron_g2p_en_no_space/40epoch.pth",
        vocoder_tag="parallel_wavegan/ljspeech_style_melgan.v1",
    )

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
        inference(text2speech)
    elif app_mode == "Source code":
        st.code(read_file(args.app_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Streamlit Tacotron2 Demo')
    parser.add_argument('--app-path', type=str, default='egs2/ljspeech/tts1/app.py', help='app path')
    args = parser.parse_args()
    main(args)