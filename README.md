# tess-train

python version 3.9.19

# deps

```bash
sudo apt-get install -y wget unzip bc vim libleptonica-dev
sudo apt-get install -y --reinstall make # 4.2+
sudo apt-get install -y g++ autoconf automake libtool pkg-config libpng-dev libjpeg8-dev libtiff5-dev libicu-dev libpango1.0-dev autoconf-archive
sudo apt-get install libgirepository1.0-dev
sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev
wget https://github.com/tesseract-ocr/tesseract/archive/4.1.0.zip
unzip 4.1.0.zip
rm -rf 4.1.0.zip
cd tesseract-4.1.0/
./autogen.sh
./configure
make -j4
sudo make install
sudo ldconfig
sudo make training
sudo make training-install
cd /usr/local/share/tessdata
sudo wget https://github.com/tesseract-ocr/tessdata_best/raw/main/fas.traineddata
export TESSDATA_PREFIX=/usr/local/share/tessdata
pip install -r requirements.txt
```

# data 
note that these are assumed to be word images, if they are not just detect and crop them.
```bash
data/
        ground-truth/
                {idx}.png|.tiff # contains image
                {idx}.gt.txt # contains ocr label text
        validation/
                {idx}.png|.tiff
                {idx}.gt.txt
```


# train
```bash
cd tesseract-4.1.0
git clone https://github.com/tesseract-ocr/tesstrain
cd ..
mkdir -p  tesseract-4.1.0/tesstrain/data/parsi-ground-truth
rsync -a ./data/ground-truth/ tesseract-4.1.0/tesstrain/data/parsi-ground-truth/
cd tesseract-4.1.0/tesstrain
```

## page segmentation mode
Set correct psm according to tesseract for training:

PSM                Page segmentation mode. Default: 13
```bash
user@Workstation:~$ tesseract --help-psm
Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.
```
Based on the info we select 8 for single words.

```bash
sudo make training MODEL_NAME=parsi START_MODEL=fas PSM=8 TESSDATA=/usr/local/share/tessdata MAX_ITERATIONS=100000 EPOCHS=100000 -j32
sudo cp data/parsi.traineddata /usr/local/share/tessdata
```

# test

```bash
python infer.py parsi
```
