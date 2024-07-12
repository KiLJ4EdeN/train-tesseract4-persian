import os
import shutil

src_dir = 'mjsynth_format_dataset' # IMPORTANT: this assumes this is also split into ['ground-truth', 'validation']
dst_dir = 'data'
sub_dirs = ['ground-truth', 'validation']

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
os.makedirs(dst_dir, exist_ok=True)
for sub_dir in sub_dirs:
    os.makedirs(os.path.join(dst_dir, sub_dir), exist_ok=True)

def process_files(sub_dir):
    src_sub_dir = os.path.join(src_dir, sub_dir)
    dst_sub_dir = os.path.join(dst_dir, sub_dir)
    
    for filename in os.listdir(src_sub_dir):
        try:
            if filename.endswith('.jpg'):
                counter, label = filename.split('_', 1)
                label = label.replace('.jpg', '')
                
                new_image_filename = f'{counter}.png'
                new_label_filename = f'{counter}.gt.txt'
                
                src_image_path = os.path.join(src_sub_dir, filename)
                dst_image_path = os.path.join(dst_sub_dir, new_image_filename)
                dst_label_path = os.path.join(dst_sub_dir, new_label_filename)
                
                shutil.copyfile(src_image_path, dst_image_path)
                
                with open(dst_label_path, 'w') as label_file:
                    label_file.write(label)
        except ValueError:
            print(filename)

for sub_dir in sub_dirs:
    process_files(sub_dir)

print("done")
