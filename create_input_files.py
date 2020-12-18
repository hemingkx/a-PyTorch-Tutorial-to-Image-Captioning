from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr30k',
                       karpathy_json_path='./caption_datasets/dataset_flickr30k.json',
                       image_folder='../Data/flickr30k/flickr30k-images/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='./data/',
                       max_len=50)
