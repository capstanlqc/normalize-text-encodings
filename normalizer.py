import argparse
import json
import html

# parse arguments
parser = argparse.ArgumentParser(description="Normalize mixed-encoding text in a JSON file.")
parser.add_argument('-i', '--input', required=True, help='Path to input JSON file')
parser.add_argument('-o', '--output', required=True, help='Path to output JSON file')

args = parser.parse_args()

# load the input JSON file
with open(args.input, 'r', encoding='utf-8') as f:
    data = json.load(f)

# normalize the text
data['text'] = html.unescape(data['text'])

# save the result to the output file
with open(args.output, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
