from bs4 import BeautifulSoup
import json

d = []

with open('reascript.html', 'r') as f:
    html_lines = f.readlines()

    tag_open = False    
    language_functions = {}
    other_text = []

    for line in html_lines:
        soup = BeautifulSoup(line, 'html.parser')
    
        if "</div>View:" in line:
            print('found the end!')
        else:
            a_els = soup.find_all('a')
            if a_els:
                a = a_els[0]
                name = a.get('name')
                if name and len(language_functions) != 0:
                    d.append({
                        'name' : name,
                        'langs' : language_functions,
                        'dist' : 0
                        # 'other_text' : other_text
                    })
                    language_functions = {}
                    other_text = []
            

            # Add the subsequent lines
            # text = soup.get_text().rstrip().lstrip().replace('\n', '')
            # if text != "":
            div_els = soup.find_all('div')
            for div in div_els:
                css_class = div.get('class')[0]
                language_functions[css_class] = line
            # if not '<div>' in line:
            #     other_text.append(line)
            
output = {'data' : d}
with open('static/api.json', 'w') as f:
    json.dump(output, f, indent=4)