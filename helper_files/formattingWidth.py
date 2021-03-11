# import 
from IPython.core.display import display, HTML, Markdown

def myHTML(text):
    ss = '''<span style='font-size:16.0pt;color:black;font-family:"Times New Roman";'>'''
    es = "</span>"
    return display(HTML(f"{ss}{text}{es}"))
    
def myHTMLreplace(text,word=''):
    ss = '''<span style='font-size:12.0pt;color:black;font-family:"Times New Roman";'>'''
    es = "</span>"
    for words in [word.lower(), word.title()]:
        if words in text:
            text = text.replace(words,f"{es}<span style='background-color:#6DB423;color: white';>{words}</span>{ss}")
            return display(HTML(f"{ss}{text}{es}"))

def set_css_style(css_file_path):
    """
    Read the custom CSS file and load it into Jupyter.
    Pass the file path to the CSS file.
    """

    styles = open(css_file_path, "r").read()
    s = '<style>%s</style>' % styles     
    return HTML(s)    
    
def hideCode():
    '''
    hideCode() - styling function for jupyter notebook
    no Input
    Output: JavaScript styling, create button to toggle code
    '''

    HTML('''<script>
            code_show=true; 
            function code_toggle() {
             if (code_show){
             $('div.input').hide();
             } else {
             $('div.input').show();
             }
             code_show = !code_show
            } 
            $( document ).ready(code_toggle);
            </script>
            <form action="javascript:code_toggle()" id="topdiv"><input type="submit" value="Click here: Toggle on/off code."></form>''')