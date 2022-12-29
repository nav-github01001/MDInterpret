import re
import os
from typing import List, Optional
html_template = """<!DOCTYPE html>
<html>
    <head>
        <title>{}</title>
    </head>
    <body>
        {}
    </body>
</html>
"""

def parse_content(contents:List[str]) -> str:
    body = """"""    
    contents = [content.strip("\n") for content in contents]
    print(contents)
    for content in contents:
        # Heading
        headings = re.findall(r'\A#.+',content)
        
        heading:str = headings[0] if len(headings) == 1 else None
        if heading:
            if heading.startswith("####"):
                body += f"<h4>{heading.removeprefix('####')}</h4>\n\t\t"
            elif heading.startswith("###"):
                body += f"<h3>{heading.removeprefix('###')}</h3>\n\t\t"
            elif heading.startswith("##"):
                body += f"<h2>{heading.removeprefix('##')}</h2>\n\t\t"
            elif heading.startswith("#"):
                body += f"<h1>{heading.removeprefix('#')}</h1>\n\t\t"
        else:
            #if it is a paragraph
            body += f"<p>{content}</p>\n\t\t"
    return body

def write_to_file(body,name,output_dir):
    with open(output_dir,'w')as out:
        out.write(html_template.format(name,body))
        print("Write Finished")


def setup()-> None:
    print("Welcome to MDinterpret! (Press Ctrl+C to exit)")    
    print("A MarkDown->HTML conversion utility")
    while True:
        file = input("File to convert to HTML? (full path) : ")
        out_path = input("Output Directory?: ")

        fileout_name=os.path.splitext(os.path.basename(file))[0]
        out = f"{out_path}/{fileout_name}.html"
        with open(file,'r') as f:
            print("Reading...")
            write_to_file(parse_content(f.readlines()),fileout_name,out)
            break
                

    
if __name__ == '__main__':
    setup()

