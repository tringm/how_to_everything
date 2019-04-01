## Google Drive

1.  Download large file from google drive

    1.  This file should be made public
    2.  Get the shareable link to get the file id
        -   E.g: links: `https://drive.google.com/open?id=11Zamj_r2cnXVTXivRclgCV-_0MZqENxU`
        -   ID: `11Zamj_r2cnXVTXivRclgCV-_0MZqENxU`
    3.  Use wget (tested, works):
        ```bash
        FILENAME="some_name"
        FILEID="file_id"
        wget --no-check-certificate "https://drive.google.com/uc?export=download&id=${FILEID}" -O $FILENAME
        ```
    4.  Use curl (tested, does not work):

        ```bash
        curl -c cookies.txt -s -L "https://drive.google.com/uc?export=download&id=${FILEID}" \
        | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt

        curl -L -b cookies.txt -o $FILENAME \
             "https://drive.google.com/uc?export=download&id='$FIELDID'&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${FILEID}"

        rm -f confirm.txt cookies.txt
        ```
