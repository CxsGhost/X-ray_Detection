from tensorflow.keras import preprocessing
img_gene = preprocessing.image_dataset_from_directory('./vae/img_data',
                                                      labels=None,
                                                      label_mode=None,
                                                      color_mode='grayscale',
                                                      batch_size=2,
                                                      image_size=(640, 640))

img_gene = preprocessing.image.ImageDataGenerator()
