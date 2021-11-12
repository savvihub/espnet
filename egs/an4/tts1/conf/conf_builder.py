# load configuration yaml
import os

import yaml

with open("conf/train_pytorch_tacotron2.yaml") as f:
    params = yaml.load(f, Loader=yaml.Loader)

# change hyperparameters by yourself!
params.update({
    "embed-dim": int(os.environ.get("embed-dim", 512)),
    "elayers": int(os.environ.get("elayers", 1)),
    "eunits": int(os.environ.get("eunits", 512)),
    "econv-layers": int(os.environ.get("econv-layers", 1)),
    "econv-chans": int(os.environ.get("econv-chans", 512)),
    "econv-filts": int(os.environ.get("econv-filts", 5)),
    "dlayers": int(os.environ.get("dlayers", 1)),
    "dunits": int(os.environ.get("dunits", 512)),
    "prenet-layers": int(os.environ.get("prenet-layers", 1)),
    "prenet-units": int(os.environ.get("prenet-units", 256)),
    "postnet-layers": int(os.environ.get("postnet-layers", 1)),
    "postnet-chans": int(os.environ.get("postnet-chans", 512)),
    "postnet-filts": int(os.environ.get("postnet-filts", 5)),
    "adim": int(os.environ.get("adim", 256)),
    "aconv-chans": int(os.environ.get("aconv-chans", 32)),
    "aconv-filts": int(os.environ.get("aconv-filts", 15)),
    "reduction-factor": int(os.environ.get("reduction-factor", 2)),
    "batch-size": int(os.environ.get("batch-size", 128)),
    "epochs": int(os.environ.get("epochs", 100)),
    "report-interval-iters": int(os.environ.get("report-interval-iters", 200)),
})

# save
with open("conf/tacotron2_config.yaml", "w") as f:
    yaml.dump(params, f, Dumper=yaml.Dumper)
