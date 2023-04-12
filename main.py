import os
os.environ["OPENAI_API_KEY"] = 'MY_KEY_HERE'

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

# save to disk
index.save_to_disk('index.json')
# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

print(index.query("generate a table showing me how much per day i spend on office stuff"))
