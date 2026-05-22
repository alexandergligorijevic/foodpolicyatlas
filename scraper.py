{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;\f1\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf0 import requests
\f1\fs24 \
\

\f0\fs26 url = "https://atlas.foodbanking.org/wp-content/uploads/country-data.xml"
\f1\fs24 \
\

\f0\fs26 r = requests.get(url, timeout=30)
\f1\fs24 \
\

\f0\fs26 r.raise_for_status()
\f1\fs24 \
\

\f0\fs26 with open("country-data.xml", "w", encoding="utf-8") as f:
\f1\fs24 \
\

\f0\fs26     f.write(r.text)
\f1\fs24 \
\

\f0\fs26 print("Downloaded XML successfully")}