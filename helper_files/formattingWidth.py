# import 
from IPython.core.display import display, HTML, Markdown

def formatting_width():
    '''
    formatting_width() - styling function for jupyter notebook
    no Input
    Output: HTML styling, page width of 70%
    '''
    HTML('''<style>

    .container { 
        width:70% !important; 
        }

    #topdiv {
        position: fixed;
        top: 100;
        left: 0;
    }

    input[type="submit"] {
        padding: 10px 10px 11px !important;
        font-size: 14px !important;
        background-color: #681796;
        font-weight: bold;
        text-shadow: 0px 2px black;
        color: #ffffff;
        border-radius: 50px;
        -moz-border-radius: 50px;
        -webkit-border-radius: 50px;
        border: 2px solid #9220d4;
        cursor: pointer;
        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
        -moz-box--shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
        -webkit-box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
        outline: 0 !important;
    }

    input[type="submit"]:hover {
        padding: 10px 10px 11px !important;
        font-size: 14px !important;
        background-color: #9220d4;
        font-weight: bold;
        text-shadow: 0px 2px black;
        color: #ffffff;
        border-radius: 50px;
        -moz-border-radius: 50px;
        -webkit-border-radius: 50px;
        border: 2px solid #681796;
        cursor: pointer;
        box-shadow: 0 2px 0 rgba(255, 255, 255, 0.5) inset;
        -moz-box-shadow: 0 2px 0 rgba(255, 255, 255, 0.5) inset;
        -webkit-box-shadow: 0 2px 0 rgba(255, 255, 255, 0.5) inset;
        outline: 0 !important;
    }

    h1 {
        color: blue;
        display: block;
        font-size: 2em;
        margin-top: 0.67em;
        margin-bottom: 0.67em;
        margin-left: 0;
        margin-right: 0;
        font-weight: bold;
        font-variant: small-caps;
    }
    h2 {
        color: #0e9aa7;
        color: #3da4ab;
        display: block;
        font-size: 1.5em;
        margin-top: 0.83em;
        margin-bottom: 0.83em;
        margin-left: 0;
        margin-right: 0;
        font-weight: bold;
        font-variant: small-caps;
    }
    h3 { 
        color: #3da4ab;
        display: block;
        font-size: 1.17em;
        margin-top: 1em;
        margin-bottom: 1em;
        margin-left: 0;
        margin-right: 0;
        font-weight: bold;
    }
    h4 { 
        color: #7732a8;
        display: block;
        margin-top: 0.1em !important;
        margin-bottom: 0.1em !important;
        margin-left: 0;
        margin-right: 0;
        padding: 0px !important;
        border: 0 !important;
        font-weight: bold;
    }
    h5 { 
        color: #fe8a71;
        display: block;
        font-size: .83em;
        margin-top: 1.67em;
        margin-bottom: 1.67em;
        margin-left: 0;
        margin-right: 0;
        font-weight: bold;
    }
    h6 { 
        display: block;
        font-size: .67em;
        margin-top: 2.33em;
        margin-bottom: 2.33em;
        margin-left: 0;
        margin-right: 0;
        font-weight: bold;
    }

    a {
      color: hotpink !important;
    }
    </style>''')
    
    
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