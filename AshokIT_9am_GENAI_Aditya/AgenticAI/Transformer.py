# import sys
# import subprocess

# # Check if it exists in the current environment
# try:
#     import transformers
#     print(f"Transformers version: {transformers.__version__}")
#     print(f"Located at: {transformers.__file__}")
# except ImportError:
#     print("Transformers not found in this environment.")
#     print(f"Current Python path: {sys.executable}")

from transformers import AutoTokenizer
tokenizer=AutoTokenizer.from_pretrained("bert-base-uncased")
text="tokenization is amazing and love, and happieness"
tokens=tokenizer.tokenize(text) #BPE
print(tokens)
ids=tokenizer.convert_tokens_to_ids(tokens)
print(ids)
#[19204]->[o.1, 0.234, 0.00896] # embedding or vectorization
