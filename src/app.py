from flask import Flask, request, jsonify
import numpy as np
from generate import batch_model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False #ソートをそのまま

@app.route('/api/conditional/samples', methods=['GET'])
def conditional_samples():
    raw_text = request.args.get('raw_text', default=None, type=str)
    nsamples = request.args.get('nsamples', default=1, type=int)
    length = request.args.get('length', default=None, type=int)
    top_k = request.args.get('top_k', default=0, type=int)
    model_name = request.args.get('model_name', default='117M', type=str)
    seed = request.args.get('seed', default=None, type=int)
    batch_size = request.args.get('batch_size', default=1, type=int)
    temperature = request.args.get('temperature', default=1, type=int)
    
    samples = []
    for sample in batch_model(
        nsamples=nsamples,
        raw_text=raw_text,
        top_k=top_k,
        length=length,
        model_name=model_name,
        seed=seed,
        batch_size=batch_size,
        temperature=temperature
        ):
        samples.append(sample)
    return jsonify(samples)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)