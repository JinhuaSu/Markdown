# nlp text analyse
## key word
**feature**
- tf: word frequency in this document
- idf: this word appearing frequency in all documents(using jieba's own internet corpus)
- textrank(based on pagerank)
    + get segment of the text
    + moving window with certain span to build relationship graph

**application**
- find tags and find key entity

**api**
jieba.analyse.extract_tags
jieba.analyse.textrank

## part-of-speech tagging
**posseg**

