from wtforms.widgets import TextInput, PasswordInput, HTMLString


class OptIconTextInput(TextInput):
    text = '%s'

    def __init__(self, name="", icon=False):
        super(OptIconTextInput, self).__init__()
        if icon:
            self.text = '<i class="fa %s"></i>'
        self.text = self.text % (name)

    def __call__(self, field, **kw):
        open_html = '''
            <div class="input-group">
                <div class="input-group-addon">%s</div>
            ''' % (self.text)
        input_html = super(OptIconTextInput, self).__call__(field, **kw)
        end_html = '</div>'
        return HTMLString("%s %s %s" % (open_html, input_html, end_html))


class OptIconPasswordInput(PasswordInput):
    text = '%s'

    def __init__(self, name="", icon=False):
        super(OptIconPasswordInput, self).__init__()
        if icon:
            self.text = '<i class="fa %s"></i>'
        self.text = self.text % (name)

    def __call__(self, field, **kw):
        open_html = '''
            <div class="input-group">
                <div class="input-group-addon">%s</div>
            ''' % (self.text)
        input_html = super(OptIconPasswordInput, self).__call__(field, **kw)
        end_html = '</div>'
        return HTMLString("%s %s %s" % (open_html, input_html, end_html))
