# xml2json

Just a tiny Python utility to convert an XML file to JSON.

## Install
```
$ git clone https://github.com/vesche/xml2json
$ cd xml2json/
$ pip install -r requirements.txt
```

## Usage
```
$ python xml2json.py --help
usage: xml2json.py [-h] -i INPUT -o OUTPUT

XML to JSON converter

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file

$ python xml2json.py -i foo.xml -o bar.json
```
