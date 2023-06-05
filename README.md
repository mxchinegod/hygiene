# hygiene 🪥

## 😅 Huh?

hygiene (🪥) is a data preprocessing toolkit that makes it easy to create common LLM-related data structures; from training data to chain payloads!

## 🤔 Why?

0. Compress (or freeze/reformat) payloads during inference and vector embedding.

1. Get data to look _the way language models expect it to look during prompting_ **no matter the origin or shape of that data** <small>while also being as small as possible</small> (which starts w/ fine-tunining engineer's goal)

2. Provide utilities and connectors to reduce code in language model workflows.

3. Prompt-generated datasets<sup>[2] [3]</sup> in particular are unique but come with similar mundane routines as others.


## 💾 Installation

``` bash
pip install hygiene-dm
```
or 
``` bash
python3 setup.py install
```



## 🤷 Usage

``` python
Python 3.11.2 (main, Mar 24 2023, 00:16:47) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hygiene
>>> from hygiene import Singleton
>>> # Example JSON string
>>> singletons = [
        {"name": "John", "age": 30, "city": "New York"},
        '{"name": "John", "age": 30, "city": "New York"}',
        list({"name": "John", "age": 30, "city": "New York"}),
        [{"name": "John", "age": 30, "city": "New York"}]
    ]
>>> qdrant_payload_examples = [
        {"count": 10, "sizes": [35, 36, 38]},
        {"price": 11.99,"ratings": [9.1, 9.2, 9.4]},
        {"is_delivered": True,"responses": [False, False, True, False]},
        {"name": "Alice","friends": ["bob","eva","jack"]},
        {"location": {"lon": 52.5200,"lat": 13.4050},
            "cities": [
                {"lon": 51.5072,"lat": 0.1276},
                {"lon": 40.7128,"lat": 74.0060}
            ]
        }
    ]
>>> def calculate_ratio(string, json_obj):
        string_size = len(string.encode('utf-8'))
        json_size = len(json.dumps(json_obj).encode('utf-8'))
        ratio = string_size / json_size
        print(f'JSON->YAML bytes ratio: {ratio}')
>>> boxing = Singleton.boxing()
>>> for each in singletons:
         package = boxing.Payload(data=each, fmt="yml")
         payload = package.deliver()
         print(payload)
         calculate_ratio(payload, each)
age: 30
city: New York
name: John

JSON->YAML bytes ratio: 0.723404255319149
age: 30
city: New York
name: John

JSON->YAML bytes ratio: 0.576271186440678
- name
- age
- city

JSON->YAML bytes ratio: 0.8695652173913043
- age: 30
  city: New York
  name: John

JSON->YAML bytes ratio: 0.8163265306122449
>>> for each in qdrant_payload_examples:
         package = boxing.Payload(data=each, fmt="yml")
         payload = package.deliver()
         print(payload)
         calculate_ratio(payload, each)
count: 10
sizes:
- 35
- 36
- 38

JSON->YAML bytes ratio: 0.8888888888888888
price: 11.99
ratings:
- 9.1
- 9.2
- 9.4

JSON->YAML bytes ratio: 0.9090909090909091
is_delivered: true
responses:
- false
- false
- true
- false

JSON->YAML bytes ratio: 0.953125
friends:
- bob
- eva
- jack
name: Alice

JSON->YAML bytes ratio: 0.7692307692307693
cities:
- lat: 0.1276
  lon: 51.5072
- lat: 74.006
  lon: 40.7128
location:
  lat: 13.405
  lon: 52.52

JSON->YAML bytes ratio: 0.8512396694214877
```

## 🥅 Goals

- Provide an extremely robust, complete, dataset for finetuning a **small language model** on payload structures<sup>[2]</sup>
- Create a fine-tuning dataset for Seq2Seq inference based on collation of the previous dataset<sup>[2]</sup>
- Use datasets to make models for embedding vectors and training LLMs on pristine "Instruct"-type chains-of-thought<sup>[3]</sup>
- Provide all of the preprocessing tools to do this within this very package

### ⚡️ Advantages

- suits structured to non-structured data but **also careless** data 👉 natural language workflows
- atomized, low-level conversions for items belonging to massive datasets (memory-safe if used correctly)
- tiny footprint in your project with _few_ dependencies
- super-easy
- fast

## ⌨️ Working on

- [ ] integrating with Qdrant
- [ ] integrating with embeddings<sup>[1]</sup>
- [x] finishing this readme
- [x] pip package

<hr>

### ✍️ Citations

[1] **"MTEB: Massive Text Embedding Benchmark"**

_Niklas Muennighoff_

https://github.com/huggingface/blog/blob/main/mteb.md

[2] **"Baize: An Open-Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data"**

_Xu, Canwen and Guo, Daya and Duan, Nan and McAuley, Julian_

https://arxiv.org/abs/2304.01196

[3] **"Training language models to follow instructions with human feedback"**

_Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe_

https://arxiv.org/abs/2203.02155
