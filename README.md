# tess-train

python version 3.9.19

# deps

```bash
sudo apt-get install -y wget unzip bc vim libleptonica-dev
sudo apt-get install -y --reinstall make # 4.2+
sudo apt-get install -y g++ autoconf automake libtool pkg-config libpng-dev libjpeg8-dev libtiff5-dev libicu-dev \
        libpango1.0-dev autoconf-archive
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
sudo mkdir -p  tesseract-4.1.0/tesstrain/data/parsi-ground-truth
sudo cp -a ./data/ground-truth/* tesseract-4.1.0/tesstrain/data/parsi-ground-truth/.
cd tesseract-4.1.0/tesstrain
```

```bash
sudo make training MODEL_NAME=parsi START_MODEL=fas TESSDATA=/usr/local/share/tessdata
sudo cp data/parsi.traineddata /usr/local/share/tessdata
```

# test

```bash
python infer.py parsi
```
