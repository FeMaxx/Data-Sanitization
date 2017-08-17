#!/usr/bin/env python
# -*- coding: utf-8 -*-

import distance

#variable for the path of the files 
file_1 = "PathOfFileWithOriginalData"
file_2 = "PathOfFileWithSanitizationData"

#open the files to read
arq_1 = open('file_1', 'r')
binarios_1 = arq_1.read()

arq_2 = open('file_2', 'r')
binarios_2 = arq_2.read()


#convert the string format to int format
binarios_originais = int(binarios_1)
binarios_sanitizados = int(binarios_2)


#result of comparison
distance.hamming("binarios_originais","binarios_sanitizados")
