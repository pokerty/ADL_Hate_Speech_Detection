#imports
from preproccessing import Preprocess

if __name__ == "__main__":
    preproccessed_data = Preprocess('\HASOC\english_dataset.tsv','\t')
    #saving the preprocessed data
    preproccessed_data.save()
