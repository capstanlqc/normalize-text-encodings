# Normalize Text Encodings

This is a simple proof of concept to show how different encodings can be normalized using Python. Other languages offer similar approaches.

## Mixed encoding input

The JSON file `file.json` has the following content: 

```JSON
{
  "text": "S&uuml;leyman \u00FCz\u00FCm yüzüğü beğendi" 
}
```

The character `ü` is encoded in three different ways: 
- as Unicode text: `ü`
- as a Unicode escape: `\u00FC`
- as an HTML named entity: `&uuml`

## Normalization

That mix of encodings may need to be normalized to have one single encoding and simplify processing by different applications. 

The script provided shows a naïve approach to do that: 

```bash
python normalizer.py -i file.json -o normalized.json
```

The result: 

```JSON
{
  "text": "Süleyman üzüm yüzüğü beğendi"
}
```
