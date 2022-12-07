import os
import random

from PIL import Image


def get_file_paths(folder):
    image_file_paths = []
    for root, dirs, filenames in os.walk(folder):
        filenames = sorted(filenames)
        for filename in filenames:
            input_path = os.path.abspath(root)
            file_path = os.path.join(input_path, filename)
            if filename.endswith('.png') or filename.endswith('.jpg'):
                image_file_paths.append(file_path)

        break  # prevent descending into subfolders
    random.shuffle(image_file_paths)
    return image_file_paths

emotion_label = {'neutral':0, 'joy':1, 'anger':2, 'disgust':3, 'surprise':4, 'fear':5}

def align_images(a_file_paths, b_file_paths, target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for i in range(len(a_file_paths)):
        img_a = Image.open(a_file_paths[i])
        img_b = Image.open(b_file_paths[i])
        tag_a = a_file_paths[i].split('/')[-1].split('_')[1]
        tag_b = b_file_paths[i].split('/')[-1].split('_')[1]

        label_a = emotion_label[tag_a]
        label_b = emotion_label[tag_b]

        assert(img_a.size == img_b.size)

        aligned_image = Image.new("RGB", (img_a.size[0] * 2, img_a.size[1]))
        aligned_image.paste(img_a, (0, 0))
        aligned_image.paste(img_b, (img_a.size[0], 0))
        aligned_image.save(os.path.join(target_path, '{:04d}_{}_{}.jpg'.format(i+1500,label_a,label_b)))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dataset-path',
        dest='dataset_path',
        help='Which folder to process (it should have subfolders testA, testB, trainA and trainB'
    # test_a_path = os.path.join(dataset_folder, 'testA')
    # test_b_path = os.path.join(dataset_folder, 'testB')
    # test_a_file_paths = get_file_paths(test_a_path)
    # test_b_file_paths = get_file_paths(test_b_path)
    # assert(len(test_a_file_paths) == len(test_b_file_paths))
    # test_path = os.path.join(dataset_folder, 'test')

    )
    args = parser.parse_args()

    dataset_folder = args.dataset_path
    print(dataset_folder)

    # test_a_path = os.path.join(dataset_folder, 'testA')
    # test_b_path = os.path.join(dataset_folder, 'testB')
    # test_a_file_paths = get_file_paths(test_a_path)
    # test_b_file_paths = get_file_paths(test_b_path)
    # assert(len(test_a_file_paths) == len(test_b_file_paths))
    # test_path = os.path.join(dataset_folder, 'test')

    val_a_path = os.path.join(dataset_folder, 'valA')
    val_b_path = os.path.join(dataset_folder, 'valB')
    val_a_file_paths = get_file_paths(val_a_path)
    val_b_file_paths = get_file_paths(val_b_path)
    assert(len(val_a_file_paths) == len(val_b_file_paths))
    val_path = os.path.join(dataset_folder, 'val')

    train_a_path = os.path.join(dataset_folder, 'trainA')
    train_b_path = os.path.join(dataset_folder, 'trainB')
    train_a_file_paths = get_file_paths(train_a_path)
    train_b_file_paths = get_file_paths(train_b_path)
    assert(len(train_a_file_paths) == len(train_b_file_paths))
    # parent_dir = "/combined_data_part_emotions/"
    train_path = os.path.join(dataset_folder, 'train')

    align_images(val_a_file_paths, val_b_file_paths, val_path)
    # align_images(train_a_file_paths, train_b_file_paths, train_path)
