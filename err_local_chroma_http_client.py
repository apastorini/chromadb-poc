
import chromadb
import gensim

# Conectar a la base de datos ChromaDB
import chromadb
client = chromadb.HttpClient(host='localhost', port=8000)

# Crear una colección (si no existe)
collection = client.create_collection(name="embeddings")

# Descargar el modelo pre-entrenado de Word2Vec
model = gensim.models.Word2Vec.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)

# Almacenar el modelo en ChromaDB
client.store_model(collection, model, name="word2vec")

# Obtener el vector de embedding para una palabra
vector = client.get_embedding(collection, "casa")

# Buscar las palabras más similares a "casa"
similar_words = client.get_similar_words(collection, "casa", topn=10)

# Imprimir los resultados
print("Vector de embedding para 'casa':", vector)
print("Palabras más similares a 'casa':", similar_words)