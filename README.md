# GPT-2 server

Web API server for using to GPT-2 model.  
Original project is [GPT-2](https://github.com/openai/gpt-2)


## prep GPT-2

```sh
git clone https://github.com/openai/gpt-2.git && cd gpt-2
docker build --tag gpt-2 -f Dockerfile.gpu . # or Dockerfile.cpu
```

## build image

```sh
docker build --tag gpt-2-server .
```

## running

running docker

```sh
docker run -p 8080:80 -p 5000:5000 gpt-2-server 
# OR using gpu
# docker run --runtime=nvidia -p 8080:80 gpt-2-server 
# OR interactive mode
# docker run -p 8080:80 -it gpt-2-server bash
```

and invoke api.

```sh
curl -v -X GET "http://localhost:8080/api/conditional/samples?top_k=40&length=200&nsamples=5&raw_text=business+japan+usa"
```

## API specification

### GET /api/conditional/samples

#### parameters

- top_k: Integer value controlling diversity. 1 means only 1 word is considered for each step (token), resulting in deterministic completions, while 40 means 40 words are considered at each step. 0 (default) is a special setting meaning no restrictions. 40 generally is a good value.
- length: Number of tokens in generated text, if None (default), is determined by model hyperparameters
- nsamples: Number of samples to return total
- model_name: 117M or 345M, which model to use
- seed:  Integer seed for random number generators, fix seed to reproduce results
- batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
- temperature=1 : Float value controlling randomness in boltzmann distribution. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.
- raw_text: Context tokens for condition of generating samples.
  
#### request example

```sh
curl -v -X GET "http://localhost:8080/api/conditional/samples?top_k=40&length=200&nsamples=5&raw_text=business+japan+usa"
```
