## I. Produce Images
1. Video all angles of the object. Make sure to center the object (region of interest or roi) and be consistent. | Camera: Mobile phone  
2. Edit the video and remove uncentered objects. | Editor: Openshot Video Editor
3. Extract the images from the video using extract.py

### Crop and Reduce File Size 
* Use batch image processing software. | Editor: XNConvert

### Gray Scale Script >> Both for positives and negatives
* $ python3 greyscale.py inputfolder outputfolder 

## II. | Auto specify folders and filenames within
$ find ./neg -iname "*.jpg" > negatives.txt
$ find ./pos -iname "*.jpg" > positives.txt

## III. | Auto specify coordinates / boundaries
$ opencv_annotation --annotations=annotations.txt --images=positive 

press c to accept selection
press n to go next
press esc to quit

## IV. | Create Postive.Vec 
$ opencv_createsamples -info annotations.txt -num 400 -w 32 -h 32 -vec positives.vec

## V. | Train 
$ opencv_traincascade -data model -vec positives.vec -bg negatives.txt -numPos 400 -numNeg 47 -numStages 4 -w 32 -h 32
