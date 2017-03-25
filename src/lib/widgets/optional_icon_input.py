from wtforms.widgets import TextInput, PasswordInput, HTMLString


class OptionalIconTextInput(TextInput):
    text = '%s'

    def __init__(self, name="", icon=False):
        super(OptionalIconTextInput, self).__init__()
        if icon:
            self.text = '<i class="fa %s"></i>'
        self.text = self.text % (name)

    def __call__(self, field, **kwargs):
        open_html = '''
            <div class="input-group">
                <div class="input-group-addon">%s</div>
            ''' % (self.text)
        input_html = super(OptionalIconTextInput, self).__call__(field, **kwargs)
        end_html = '</div>'
        return HTMLString("%s %s %s" % (open_html, input_html, end_html))


class OptionalIconPasswordInput(PasswordInput):
    text = '%s'

    def __init__(self, name="", icon=False):
        super(OptionalIconPasswordInput, self).__init__()
        if icon:
            self.text = '<i class="fa %s"></i>'
        self.text = self.text % (name)

    def __call__(self, field, **kwargs):
        open_html = '''
            <div class="input-group">
                <div class="input-group-addon">%s</div>
            ''' % (self.text)
        input_html = super(OptionalIconPasswordInput, self).__call__(field, **kwargs)
        end_html = '</div>'
        return HTMLString("%s %s %s" % (open_html, input_html, end_html))
