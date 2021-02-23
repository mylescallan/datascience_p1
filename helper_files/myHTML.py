class Todo:
    def __init__(self):
        self.items = []

    def add(self, text, completed):
        self.items.append({'text': text, 'completed': completed})

    def _repr_html_(self):
        return '''<script>
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
                    <form action="javascript:code_toggle()" id="topdiv"><input type="submit" value="Click here: Toggle on/off code."></form>'''