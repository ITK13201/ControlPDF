# ControlPDF

## introduction

PDFファイルを結合，分割できるようなツールを作りました．

## How to use

単一ファイル化してあるので，`dist`ディレクトリ内の`ControlPDF`ファイルを`./ControlPDF`で実行するだけで使えます．非破壊的プログラムです．

## Combine

PDFファイルの結合についてです．

### example


実行前のディレクトリのツリーです．
```
.
├── 01.pdf
├── 02.pdf
└── ControlPDF

0 directories, 3 files
```
以下のコマンドを実行

```bash
$ ./ControlPDF
```
実行中
```
# Combine or Split [c/s]: c
# How many pdfs?: 2
### Input filename. ###
# pdf[1]: 01
# pdf[2]: 02
# created_filename: 01-02
### Completed! ###
```
実行後のディレクトリのツリーです．
```
.
├── 01-02.pdf
├── 01.pdf
├── 02.pdf
└── ControlPDF

0 directories, 4 files
```

## Split

PDFファイルの分割についてです．

### example


実行前のディレクトリのツリーです．
```
.
├── 01.pdf
└── ControlPDF

0 directories, 2 files
```
以下のコマンドを実行

```bash
$ ./ControlPDF
```
実行中
```
# Combine or Split [c/s]: s
# Input filename: 01
### Input first and last page number to be splited. ###
# first number: 2
# last number: 3
# created_filename: 01_2-3
### Completed! ###
```
実行後のディレクトリのツリーです．
```
.
├── 01.pdf
├── 01_2-3.pdf
└── ControlPDF

0 directories, 3 files
```