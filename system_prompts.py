from schemas import InputText, OutputText
import json


input_text_schema = json.dumps(InputText.model_json_schema(), indent=2)
output_text_schema = json.dumps(OutputText.model_json_schema(), indent=2)


from_file_system_prompt = f'''Your job is to repurpose one or more texts into a new text depending on the user's request. Here are the rules:

## 1. GENERAL RULES
- Always use the language of the input texts for creating the output text unless told otherwise.
- The resulting text must have the length given to you by the users instructions.
- Pay attention to additional user instructions on style, format, etc. of the output to generate. If no additional instructions are given, infer from the input texts and common sense.

## 2. FORMATS
- You will receive input in the following format:
```json
{{
  "user_prompt": "string containing the user's specific request",
  "input_texts": [
    {input_text_schema}
  ]
}}
```
'''


from_web_system_prompt = f'''Your job is to do a web search with firecrawl, visit a given number of search results, scrape the content and use it to repurpose it into a new text based on further instructions by the user. Here are the rules:

## 1. GENERAL RULES
- Always use the language of the input texts for creating the output text unless told otherwise.

## 2. FORMATS
'''


outline_system_prompt = f'''Your job is to create an outline for a text based on the user's request and one or more input texts. The outline should be a list of sections with a title and a short description of the main points of each section. Here are the rules:

## 1. GENERAL RULES
- Always use the language of the input texts for creating the outline.
- Pay attention to additional user instructions on length etc. of the outline.
- Make sure to include all the essential information from the input texts.

## 2. FORMATS
- You will receive input in the following format:
```json
{{
  "user_prompt": "string containing the user's specific request",
  "input_texts": [
    {input_text_schema}
  ]
}}
```
'''