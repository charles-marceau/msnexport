
<p align="center">
  <img src="https://github.com/charles-marceau/msnexport/raw/master/assets/logo.png"><br>
</p>

## About
MSNexport is a command line tool to export your old MSN history files (XML) to an easy to read format (PDF).

## Installation
Install using [pip](https://pip.pypa.io/en/stable/quickstart/):

```
$ pip install msnexport
```

## Usage
To use MSNexport, all you have to do is the following command:
```
$ msnexport INPUT_FILE_PATH OUTPUT_FILE_PATH
```

Example:
```
$ msnexport john_cena753233637775.xml myConvoWithJohn.pdf
```

## How to find your history files
MSN history files are usually found on the following path:
```
C:\Documents and Settings\%USERNAME%\Documents\My received files\
```
In this folder, there should be a folder for each MSN account used on the computer. These folders contain your history files (1 file per contact).
